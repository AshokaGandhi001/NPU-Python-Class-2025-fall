import jieba

# read .txt file
txt = open("threeKingdom.txt",encoding="utf-8").read()
words = jieba.lcut(txt)
counts = {}
for word in words :
    if len(word) == 1 :
        continue
    elif word == "诸葛亮" or word == "孔明曰":
        rword = "孔明"
    elif word == "关公" or word == "云长":
        rword = "关羽"
    elif word == "玄德" or word == "玄德曰":
        rword = "刘备"
    elif word == "孟德" or word == "丞相":
        rword = "曹操"
    else :
        rword = word
    counts[rword] = counts.get(rword, 0) + 1

exclude = set({"都督","一人","陛下","魏兵","不敢","今日","引兵", "次日", "大喜",
               "将军", "却说", "二人", "不可", "荆州", "不能", "如此",
               "商议", "如何", "军士", "左右", "军马","天下", "东吴","于是"})
for word in exclude:
    del(counts[word])
item = list(counts.items())
item.sort(key= lambda x : x[1], reverse=True)

result = open("result.txt", "w",encoding="utf-8")
result.write("三国演义出现次数前10的人物：\n")
for i in range(10):
    word, count = item[i]
    result.write(word + "： " + str(count) + "\n" )
result.close

print("\n All done.")

