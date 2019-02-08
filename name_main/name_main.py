import import_file

def main():
	print("I'm being executed by python directly, hence my __name__: {}".format(__name__))

if __name__ == '__main__':
	print("Run directly")
	main()
else:
	print("Run as import")