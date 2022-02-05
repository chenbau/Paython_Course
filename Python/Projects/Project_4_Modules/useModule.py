import chenModule as blabla

def x(a_collection):

    print(type(a_collection))
    print(len(a_collection))
    print(a_collection)
    if(type(a_collection)) is list:
        a_collection.reverse()
        print(a_collection)
        # print(a_collection[-1:-len(a_collection)-1:-1]) #another way for reverse
    else:
        print("not list")


x(blabla.list_imp)
x(blabla.dictionary)

