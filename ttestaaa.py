import os
r="./data/ucf.csv"
# pa=os.path.join(r, 'ucf', 'ucf101', video_id)
# p2=r"./data\downstream\ucf\ucf101\HeadMassage\v_HeadMassage_g02_c03.avi"
p2=r"./data/downstream\ucf\ucf101\CricketBowling/v_CricketBowling_g24_c02.avi"
p4=r"data/downstream/ucf/ucf101/CricketBowling/v_CricketBowling_g24_c02.avi"
p5=r"data/downstream/ufc/ucf101/CricketBowling/v_CricketBowling_g24_c02.avi"
p3=r"data/downstream/ufc/ucf101/HeadMassage/v_HeadMassage_g02_c03.avi"
# print(os.path.isfile(p2))
# print(os.path.isfile(p3))
print(os.path.isfile(p4))
print(os.path.isfile(p5))
for i in range(70):
    print(p4[i],p5[i])
    print(p4[i]==p5[i])