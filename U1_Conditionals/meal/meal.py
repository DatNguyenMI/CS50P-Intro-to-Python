def main():
    question = input ("What time is it? ")
    question = convert(question)
    if 7 <= question <= 8:
        print ("breakfast time")
    elif 12 <= question <= 13:
        print ("lunch time")
    elif 18 <= question <=19:
        print ("dinner time")


def convert(time):
    hour, minute = time.strip().split(":")
    time = int(hour) + int(minute)/60
    return time



if __name__ == "__main__":
    main()
