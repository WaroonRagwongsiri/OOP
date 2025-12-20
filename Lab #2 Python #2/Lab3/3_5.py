empty_str = [
	'""',
	"''",
	'" "',
	"' '",
	"",
	" ",
]

accepted_prop = [
	'albumTitle',
	'artist',
	'tracks'
]

def main() -> None:
	try:
		user_input = input("Input : ").strip()
		user_input = user_input.split('|')
		rec, ids, prop, val = [x.strip() for x in user_input]

		if ids.isnumeric() == False or ids == '0':
			raise Exception
		rec = eval(rec)
		# Check record
		if type(rec) != dict:
			raise Exception
		base = rec.get(ids, None)
		if not prop in accepted_prop:
			raise Exception

		# if no id in rec
		if base == None:
			if val in empty_str:
				raise Exception
			else:
				rec[ids] = {}
				if prop == 'tracks':
					rec[ids][prop] = [val]
				else:
					rec[ids][prop] = val

		# Empty Str
		if val in empty_str:
			del rec[ids][prop]
		else:
			# If properties != tracks
			if (prop != 'tracks'):
				rec[ids][prop] = val
			# If properties == tracks
			else:
				track_prop = base.get('tracks', None)
				# If there is no tracks
				if track_prop == None:
					rec[ids][prop] = [val]
				# If there is tracks
				else:
					rec[ids][prop].append(val)
		print(rec)
	except:
		print("Invalid")
	return

if __name__ == '__main__':
	main()