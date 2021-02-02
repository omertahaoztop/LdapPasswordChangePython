import ldap
import ldap.modlist as modlist
import getpass
print('Connecting to ldap server...')
userId=input("Enter your uid: ")
user_dn='uid='+userId+',ou=users,dc=example,dc=com'
connect = ldap.initialize('your ldap host')
connect.set_option(ldap.OPT_REFERRALS, 0)
ldapPassword=getpass.getpass("Enter your ldap password:")
try:
    connect.simple_bind_s(user_dn,ldapPassword)
except ldap.NO_SUCH_OBJECT:
    print(f'Ldap username {username} not found...')
    exit(1)
except ldap.UNWILLING_TO_PERFORM as e:
    if e.args[0]['info'] == 'Unauthenticated binds are not allowed':
        print('A password is required...')
    else:
        print('Something went wrong, please try again...')
    exit(1)
except ldap.INVALID_CREDENTIALS:
    print('Password incorrect...')
    exit(1)
print('Connected!\n')
newPassword=getpass.getpass("Enter your new password:")
connect.passwd_s(user_dn,ldapPassword,newPassword)
print("Success password changing")