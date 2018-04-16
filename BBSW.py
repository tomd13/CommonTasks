import pyautogui
import datetime
import pandas as pd
import time
import pysftp


# 0.5 sec pause between pyautogui commands, move mouse to top left corner to trigger fail-safe
pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True

file_path = r'C:\Users\tdavies\PycharmProjects\untitled'


def export_trades():
    # Export trades from Nova and create csv for new trades

    # Check Nova is visible
    header_loc = pyautogui.locateCenterOnScreen(r'C:\Users\tdavies\PycharmProjects\untitled\matchID.png')
    if header_loc is None:
        return print("Can't find Match ID column header - make sure Nova blotter is visible")

    # Copy current Trade Book
    pyautogui.rightClick(header_loc)
    pyautogui.typewrite('c')
    pyautogui.press('enter')
    df_alltrades = pd.read_clipboard()

    # Compare export with previous export to identify new trades
    df_prevtrades = pd.read_csv('BBSW Prev Export.csv')
    df_newtrades = df_alltrades.copy()
    already_reg = ''
    for trade in df_alltrades.ID:
        if trade in df_prevtrades.ID.values:
            df_newtrades = df_newtrades[df_newtrades.ID != trade]
            #already_reg += (str(trade) + ' ')
    #print(str(already_reg) + ' already registered')

    # Write new trades to csv
    if not df_newtrades.empty:
        # Get run number and update run_count file
        df_runcount = pd.read_csv('run_count.csv')
        if df_runcount.Date[0] == str(datetime.date.today()):
            df_runcount.Run[0] += 1
        else:
            df_runcount.Date[0] = str(datetime.date.today())
            df_runcount.Run[0] = 1
        df_runcount.to_csv('run_count.csv', index=False)

        # Add seconds to the trade times
        df_newtrades['Exec. Date'] = df_newtrades['Exec. Date'] + ":" + str(datetime.datetime.now().second)

        # Write new trades to csv
        newtrades_filename = str(datetime.date.today()) + '-TPBBSW_' + str(df_runcount.Run[0]) + '.csv'
        df_newtrades.to_csv(newtrades_filename, index=False)
        df_alltrades.to_csv('BBSW Prev Export.csv', index=False)
        print(str(newtrades_filename) + ' successfully exported. ' + str(datetime.datetime.now()))

        #print('Sleeping for 5secs - ' + str(datetime.datetime.now()))
        #time.sleep(5)
        transfer_file(newtrades_filename)

    else:
        print('No new trades.')


def auto_run():
    # Continuously check for new trades (via red flash)
    while True:
        if not pyautogui.locateCenterOnScreen(r'C:\Users\tdavies\PycharmProjects\untitled\redflash.png') is None:
            export_trades()
            #print('Sleeping for 2.5secs - ' + str(datetime.datetime.now()))
            #time.sleep(2.5)
        time.sleep(0.1)


def transfer_file2(filename):
    # Transfer new trades file to SFTP server
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    srv = pysftp.Connection(host="https://securefiletransfer.icap.com/", username="tp-atvrep", password="bngVKTjg7CNv", cnopts=cnopts)
    srv.put(filename)
    srv.close()

def transfer_file(filename):
    # Transfer new trades file to SFTP server
    print('Sleeping for 5secs - ' + str(datetime.datetime.now()))
    time.sleep(5)
    print('Starting transfer')
    if pyautogui.locateCenterOnScreen(r'C:\Users\tdavies\PycharmProjects\untitled\SFTPAdd.png') is None:
        print('Couldn''t find the SFTP site - check that it''s visible.')
    pyautogui.click(pyautogui.locateCenterOnScreen(r'C:\Users\tdavies\PycharmProjects\untitled\SFTPAdd.png'))
    pyautogui.typewrite(str(file_path))
    pyautogui.press('enter')
    pyautogui.typewrite(str(filename))
    pyautogui.press('enter')
    pyautogui.click(pyautogui.locateCenterOnScreen(r'C:\Users\tdavies\PycharmProjects\untitled\SFTPUpload.png'))
    print('Transfer complete')
    print('Sleeping for 5secs - ' + str(datetime.datetime.now()))
    time.sleep(5)
    export_trades()


auto_run()
#export_trades()
#transfer_file('Test.csv')