
class Item:
    name= ""
    price= 0.0 #cost price for stock
    qty= 0
    sn=0
    sp= 0  #selling price

    def __init__(self, name, price, qty):
        self.name= name
        self.price= price
        self.qty= qty
        self.sp= 1.2* self.price

    def setPrice(self,price):
        self.price= price

    def setSN(self,sn):
        self.sn= sn

    def getItem(self):
        print(str(self.sn)+ ". "+ self.name + " "+ str(self.sp))

    def getItemStock(self):
        print(str(self.sn)+ ". "+ self.name + " "+ str(self.price)+ " "+ str(self.sp) + "  "+ str(self.qty))
    

item_stock= {}
sales= {}
itemTuple= ()
def addStock(item, stock):
    stock[item.sn]= item
    

def createStock():
    sn= 1

    fo = open("data.csv","r")

    for line in fo.readlines():
        data= line.split(",")
        stk= Item(data[0].strip().replace("'",""),float(data[2].strip().replace("'","")),int(data[1].strip().replace("'","")))
        stk.setSN(sn)
        addStock(stk,item_stock)
        sn+=1

    fo.close()
    

def updateStock(item, stock):
    current= stock[item.sn]
    current.qty -= item.qty
    stock[item.sn]= current

def printStock():
    print("SN"+ ". "+ "Name" + " "+ "CP" + " "+ "SP" + "  "+ "Qty")
    for key in item_stock.keys():
        item= item_stock[key]
        item.getItemStock()

def printAvalableItems():
    print("SN"+ ". "+ "Name" + " "+ "Price")
    for key in item_stock.keys():
        item= item_stock[key]
        item.getItem()

def addItem(tuple1, tuple2):
    tuple3 = tuple1 + tuple2
    #print(tuple3)
    return tuple3

def buyItems():
    global itemTuple
    i= input("Please type SN of item you want to buy\t")
    q= input("How many of this item\t")
    try:
        i_= int(i)
        q_= int(q)
        item= item_stock[i_]
        sale_item= Item(item.name,item.sp,q_)
        sale_item.setSN(i_)
        tup1= (sale_item,)
        itemTuple= addItem(itemTuple,tup1)
    except:
        print("Incorrect item or quantity entry\t")

    reply= "Y"
    while reply=="Y" or reply=="y" :
        reply= input("Do you want to buy another item (Y/N)\t")
        if reply=="Y" or reply=="y" :
            i= input("Please type SN of item you want to buy\t")
            q= input("How many of this item\t")
            try:
                i_= int(i)
                q_= int(q)
                item= item_stock[i_]
                sale_item= Item(item.name,item.sp,q_)
                sale_item.setSN(i_)
                tup1= (sale_item,)
                itemTuple= addItem(itemTuple,tup1)
            except:
                print("Incorrect item or quantity entry\t")
        else :
            break
   
            
        

def computeGain():
    gain=0.0
    for key in sales.keys():
        item= sales[key]
        try :
            stock= item_stock[item.sn]
            costpr = stock.price
            sellpr= item.price
            gain+= (sellpr-costpr)* item.qty
        except :
            print("Item " + item.name+ " does not exist in stock\t")
    print("Daily Gain = " + str(gain))
    
def computeGoodsPurchased():
    total = 0
    numItems= 0
    vat= 0.0
    vatp=0
    lprice=0     

    print("Name    Price   Quantity    Total ")
    for item in itemTuple:
        try :
            current= sales[item.sn]
            current.qty += item.qty
            sales[item.sn]= current
        except :
            sales[item.sn]= item      
        
        total += item.price * item.qty
        numItems+= item.qty
        updateStock(item,item_stock)
        if lprice==0 :
            lprice = item.price
        elif item.price<lprice :
            lprice = item.price
            
        print(item.name+ "      "+ str(item.price) +"       " + str(item.qty) + "       "+ str(item.price * item.qty))

    if numItems<5 :
        vatp= 20
        vat= 0.2 * total
    elif numItems>=10 :
        vatp= 30
        vat= 0.3 * total
    
    print("Total Amount without VAT =               " + str(total))
    print("VAT at " + str(vatp) + "% =               " + str(vat))
    print("Total Amount with VAT =               " + str(total + vat))

    if (lprice>=100 and numItems>=10):
        print("You qualify for a Bonus of N800")



createStock()
#printStock()

print("Stock Available in Adamu Retail Shop!!!!")
printAvalableItems()

buyItems()
computeGoodsPurchased()

#printStock()


computeGain()




