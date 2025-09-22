name_and_scores = input("Enter the names and scores of 3 students :")
delimeter = input('Enter characters to split :')

s1, s2, s3 = name_and_scores.split(delimeter)
s1_name, s1_score = s1.split()
s2_name, s2_score = s2.split()
s3_name, s3_score = s3.split()

s1_score = int(s1_score)
s2_score = int(s2_score)
s3_score = int(s3_score)

print("Student1 name : %s, score : %d" % (s1_name, s1_score))
print("Student2 name : %s, score : %d" % (s2_name, s2_score))
print("Student3 name : %s, score : %d" % (s3_name, s3_score))

print("Total score : %d," % (s1_score + s2_score + s3_score), 
      "Average score : %.2f" % ((s1_score + s2_score + s3_score) / 3))
