def get_sftp():
    print('sftp 작업을 시작합니다.')

def regist(name, gender, *args):
    print(f'이름: {name}')
    print(f'성별: {gender}')
    print(f'이름: {args}')


def regist2(name, gender, *args, **kwargs):
    print(f'이름: {name}')
    print(f'성별: {gender}')
    print(f'Args: {args}')
    email = kwargs.get('email')
    phone = kwargs.get('phone')
    cellphone = kwargs.get('cellphone')
    if email:
        print(email)
    if phone:
        print(phone)
    if cellphone:
        print(cellphone)



