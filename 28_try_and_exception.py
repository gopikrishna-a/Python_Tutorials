while True:
    try:
        num = int(raw_input("Enter Ur Fav Numabe: ? \n"))
        print 18/num
        break
    except ValueError:
        print "Make sure to enter a valid Number"

    except ZeroDivisionError:
        print "Don't Pick Zero"
    except:
        break
    finally:
        print "Loop completed"
