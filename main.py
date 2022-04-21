sfz = input('输入身份证前17位')

# 分别取身份证1-17位
try:
    s1 = int(sfz[0:1])
    s2 = int(sfz[1:2])
    s3 = int(sfz[2:3])
    s4 = int(sfz[3:4])
    s5 = int(sfz[4:5])
    s6 = int(sfz[5:6])
    s7 = int(sfz[6:7])
    s8 = int(sfz[7:8])
    s9 = int(sfz[8:9])
    s10 = int(sfz[9:10])
    s11 = int(sfz[10:11])
    s12 = int(sfz[11:12])
    s13 = int(sfz[12:13])
    s14 = int(sfz[13:14])
    s15 = int(sfz[14:15])
    s16 = int(sfz[15:16])
    s17 = int(sfz[16:17])

    # 通过公式法计算身份证最后一位
    j1 = s1 * 7
    j2 = s2 * 9
    j3 = s3 * 10
    j4 = s4 * 5
    j5 = s5 * 8
    j6 = s6 * 4
    j7 = s7 * 2
    j8 = s8 * 1
    j9 = s9 * 6
    j10 = s10 * 3
    j11 = s11 * 7
    j12 = s12 * 9
    j13 = s13 * 10
    j14 = s14 * 5
    j15 = s15 * 8
    j16 = s16 * 4
    j17 = s17 * 2

    # 相加求和，在求余数
    jjj = j1 + j2 + j3 + j4 + j5 + j6 + j7 + j8 + j9 + j10 + j11 + j12 + j13 + j14 + j15 + j16 + j17
    # 然后将相加的数除以11求余数
    yu = jjj % 11

    # 如果余数是10 ，身份证最后一位为2
    # 如果余数是2 ，最后一位为x
    # 如果余数是7 ，最后一位为5
    # 如果余数是5 ，最后一位为7
    # 如果余数是9 ，最后一位为3
    # 如果余数是3 ，最后一位为9
    if yu == 1:
        print('身份证前17位位:%s \n最后一位为0' % sfz)
    elif yu == 0:
        print('身份证前17位位:%s \n最后一位为1' % sfz)
    elif yu == 10:
        print('身份证前17位位:%s \n最后一位为2' % sfz)
    elif yu == 2:
        print('身份证前17位位:%s \n最后一位为x' % sfz)
    elif yu == 7:
        print('身份证前17位位:%s \n最后一位为5' % sfz)
    elif yu == 5:
        print('身份证前17位位:%s \n最后一位为7' % sfz)
    elif yu == 9:
        print('身份证前17位位:%s \n最后一位为3' % sfz)
    elif yu == 3:
        print('身份证前17位位:%s \n最后一位为9' % sfz)
    else:
        print('身份证前17位位:%s \n最后一位为%s' % (sfz, yu))





except:
    print('你输入有误')
