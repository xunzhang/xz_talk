#! /usr/bin/python
# ETL: format training data

def sample(input, output):
	fin = file(input)
	fout = file(output, 'w')
	for line in fin:
		(uid, mid, time, rating) = line.strip().split()
		if time.startswith('2003') and (int(mid) % 5 == 0):
			fout.write('%s,%s,%s\n' % (uid, mid, rating)) 
	fout.close()
	fin.close()

def format(input, output):
	fin = file(input)
	ucnt = 1
	mcnt = 1
	usr_dict = {}
	item_dict = {}
	for line in fin:
		(uid, mid, rating) = line.strip().split(',')
		if not uid in usr_dict:
			usr_dict[uid] = ucnt
			ucnt += 1
		if not mid in item_dict:
			item_dict[mid] = mcnt
			mcnt += 1
	print len(usr_dict), len(item_dict)
	fin = file(input)
	fout = file(output, 'w')
	for line in fin:
		(uid, mid, rating) = line.strip().split(',')
		fout.write('%s,%s,%s\n' % (str(usr_dict[uid]), str(item_dict[mid]), rating))
	fout.close()
	fin.close()

if __name__ == '__main__':
	sample('train', 'sample')
	format('sample', 'sample_fmt')
	
