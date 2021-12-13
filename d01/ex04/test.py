from eval import Evaluator

e = Evaluator()

print(e.enumerate_evaluate(None, None))
print(e.enumerate_evaluate([1, 2, 3], []))
print(e.enumerate_evaluate([1, 2, 3], ["word", 2, "wordo"]))

print('\n')
print(e.enumerate_evaluate([3, 8], ['Hello', 'Wolrd!'])) 
# 3 * 5 + 6 * 8 = 63
print(e.enumerate_evaluate([1, 2, 3], ["word", 'sss', "wordo"])) 
# 1 * 4 + 2 * 3 + 5 * 3 = 25

print('\n')
print(e.zip_evaluate([3, 8], ['Hello', 'Wolrd!']))
print(e.zip_evaluate([1, 2, 3], ["word", 'sss', "wordo"]))