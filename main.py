def selfDividingNumbers(left, right):
        
        newList = []
        newNum = ""  

        for x in range(left, right + 1):
            num = str(x)
            for d in num:
                # if num.index(d) != num[0] and num.count(d) > 1:
                #   newNum += d
                if d == "0":
                    newNum = ""
                    continue
                elif x % int(d) == 0:
                    newNum += d
                    if newNum == num:
                        newList.append(x)
                        newNum = ""
                    else:
                        if len(newNum) == len(num) or newNum[0] != num[0]:
                            newNum = ""
                            continue
                        else:
                            if len(num) > 2:
                                if num.index(d) > 0 and num.count(d) > 1:
                                  if newNum == num[-1] and newNum != num[0:-2]:
                                      newNum = ""
                                      continue
                                  else:
                                      continue
                                else:
                                  continue
                            else:
                                if newNum == num[-1] and newNum != num[0]:
                                    newNum = ""
                                    continue
                                else:
                                    continue
                else:
                    newNum = ""
                    break
        print('// ** Items in List: ', len(newList))

        return newList

print(selfDividingNumbers(3056, 4813))