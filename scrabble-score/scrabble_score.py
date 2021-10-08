def score(word):
	value_dict={**dict.fromkeys(list("aeioulnrst"),1),**dict.fromkeys(list("dg"),2),**dict.fromkeys(list("bcmp"),3),**dict.fromkeys(list("fhvwy"),4),**dict.fromkeys(list("k"),5),**dict.fromkeys(list("jx"),8),**dict.fromkeys(list("qz"),10),}				
	return sum((value_dict[i] for i in word.lower()))