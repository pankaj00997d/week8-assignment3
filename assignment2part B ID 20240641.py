 #AUTHOR :PANKAJ THAPA
#DATE : 2025-04-11
#ID 20240641
class RequestSystem:

    # I  make counter to get unique requisition id
    id_counter = 10000

    #  i make function with empty list to store all request.
    def __init__(self):
        self.requisitions = []

    # i make this functon for new requisition id
    def generate_requisition_id(self):
        RequestSystem.id_counter += 1  
        return RequestSystem.id_counter  

    #  this function is for store information about every requisition (staff, date, etc.)
    def user_info(self, date, staff_id, staff_name):
        requisition_id = self.generate_requisition_id()
        return {
            'date': date,  
            'requisition_id': requisition_id, 
            'staff_id': staff_id,  
            'staff_name': staff_name,  
            'items': {},  
            'total': 0,  
            'status': 'Pending',  
            'approval_reference': 'Not available'  
        }

    # from there i will add new requisition
    def staff_info(self, date, staff_id, staff_name):
        requisition = self.user_info(date, staff_id, staff_name)  
        self.requisitions.append(requisition)
        return requisition  

    #  kmow this function add items of an existing requisition and calculate the total cost of itt
    def requisition_details(self, requisition_id, items):
        for requisition in self.requisitions:  
            if requisition['requisition_id'] == requisition_id:  
                total_cost = sum(items.values()) 
                requisition['items'] = items  
                requisition['total'] = total_cost  
                return total_cost  
        return None  

    # This function will update the status of the requisition (Approved, Pending, Not Approved)
    def respond_requisition(self, requisition_id, status, approval_reference=None):
        for requisition in self.requisitions:  # Look at each requisition in the list
            if requisition['requisition_id'] == requisition_id:  # If we find the right requisition
                requisition['status'] = status  # Change the status to the new one (Approved, Pending, etc.)
                if status == 'Approved': 
                    requisition['approval_reference'] = approval_reference or f"{requisition['staff_id']}{str(requisition_id)[-3:]}"
                else:  # condition of not approved
                    requisition['approval_reference'] = 'Not available'
                return requisition 
        return None  #  i write none because of dont find the requisition

    # This function will print out all the requ
    def display_requisition(self):
        print("\nPrinting Requisitions")
        for req in self.requisitions:
            print(f"Date: {req['date']}") 
            print(f"Requisition ID: {req['requisition_id']}")
            print(f"Staff ID: {req['staff_id']}")  
            print(f"Staff Name: {req['staff_name']}")  
            print(f"Total: ${req['total']}") 
            print(f"Status: {req['status']}")  
            print(f"Approval Reference Number: {req['approval_reference']}\n")  

    #  know This function will count and print the statistics of requisitions like aprroved or pending
    def requisition_statistics(self):
        total_submitted = len(self.requisitions) 
        approved_count = sum(1 for req in self.requisitions if req['status'] == 'Approved')  
        pending_count = sum(1 for req in self.requisitions if req['status'] == 'Pending')  
        not_approved_count = sum(1 for req in self.requisitions if req['status'] == 'Not Approved')  

        # know i print reuisition statics
        print("\nDisplaying the Requisition Statistics")
        print(f"The total number of requisitions submitted: {total_submitted}")
        print(f"The total number of approved requisitions: {approved_count}")
        print(f"The total number of pending requisitions: {pending_count}")
        print(f"The total number of not approved requisitions: {not_approved_count}")


#  from here i, starts the program 
if __name__ == "__main__":
    system = RequestSystem()  #  know i Create an instance of the RequestSystem class

    #  know i Submit requisitions with details like date, staff ID, staff name, and items
    system.staff_info("15/04/2025", "K012", "Mehak jamwal")
    system.requisition_details(10001, {'item1': 150, 'item2': 300})

    system.staff_info("05/04/2025", "K032", "Shriya")
    system.requisition_details(10002, {'item1': 500, 'item2': 500})

    system.staff_info("18/05/2025", "K045", "swati")
    system.requisition_details(10003, {'item1': 3500})

    system.staff_info("13/05/2025", "K047", "palak")
    system.requisition_details(10004, {'item1': 490})

    system.staff_info("20/05/2025", "K023", "devika")
    system.requisition_details(10005, {'item1': 200, 'item2': 100})

    system.staff_info("22/05/2025", "k099", "rahul")
    system.requisition_details(10006, {'item1': 700, 'item2': 300})

    system.staff_info("28/05/2025", "K001", "Himanshi")  
    system.requisition_details(10007, {'item1': 800, 'item2': 400, 'item3': 100})

    #  for Respond to the requisitions to set their status to Approved, Pending, or Not Approved
    system.respond_requisition(10001, 'Approved', 'K04522')
    system.respond_requisition(10002, 'Pending')
    system.respond_requisition(10003, 'Not Approved')
    system.respond_requisition(10004, 'Approved', 'K043359')
    system.respond_requisition(10005, 'Approved', 'K023353')
    system.respond_requisition(10006, 'Pending')
    system.respond_requisition(10007, 'Not Approved')
    #  know getting all requisitions detail and statics
    system.display_requisition()
    system.requisition_statistics()

