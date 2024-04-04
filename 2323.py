names = (input(''). split(','))
lenth = int(input(''))
for i in names:
    if len(i) < length:
        print((str(i).lower())), end='')


 A = set(input().split())
 B = set(input().split())
 C = set(input().split())
 unique_world = B - (A/B)
min_length = min(len(world) for world in unique_worlds)
 print('-'.join(unique_worlds))
 print(min_length)

  answers = []
  index = 0
  while True
    line = input()
    if line =='100500':
       break
 numbers = list(map(int,line.split(';')))
 first_num = numbers[0]
 unique_nums=
 sorted(list(set(numbers[1:])))
 filtered_nums = [num for num in unique_nums if num % vfrst == 0]
 answer = "".join(map(str,filtered_nums))
 if index % 2 == 0:
     answer += "" + str(max(numbers))
 else:
     answer += "" + str(min(numbers))
 answers.append(answer)

 for answer in answers:
     print(answer)