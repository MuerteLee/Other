class boolIp(object):
    def __init__(self,strIp):
        dCount = 0;
        ipT = []
        if strIp.count('.') == 3:
            lenS=len(strIp) -1;
            for i in strIp:
                if i.isdigit() == False and i !=  '.':
                    print("the ip may include str, not int value")
                    return
                if strIp[0] =='.' or strIp[lenS]  == '.':
                    print("Please check your IP, the '.' is not suitable for this ip");
                    return;
                else:
                    if i.isdigit():
                        dCount =  dCount + 1
                        ipT.append(str(i))
                    elif i == '.':
                        if dCount < 4 and dCount > 0:
                            dCount = 0;
                        else:
                            print("Please check your IP num count")
                            return 

                        if int(''.join(ipT)) == 0 or int(''.join(ipT)) >= 255:
                            print("Please check you ip num, the ip may more than 255")
                            return 

                        ipT=[]
            print("OK")
        else:
            print("please check your '.' count: %d" %strIp.count('.'));
        return ;

if __name__ == "__main__":
    # Test Data
    strIp = "128.224.158.225"
    # '.' 位置不对
    strIp10=".128.224.158.224"
    strIp11=".128.224.158.224."
    strIp12="128.224..158224"
    strIp13="128.224.158224"

    #含有其他符号
    strIp20="128?224'158,224"
    strIp21="128?224.158,224"
    strIp22="128!224.158,224"
    strIp23="128`224.158,224"
    strIp24="128~224.158,224"
    strIp25="12g.224.158.224"

    #段超过3位数
    strIp30="1234.224.158.224"
    strIp31="123.2248.158.224"
    
    # 段值超过255
    strIp40="123.255.158.224"
    strIp41="123.256.158.224"

    #判断A,B,C,D,E类IP

    boolIp(strIp12)
