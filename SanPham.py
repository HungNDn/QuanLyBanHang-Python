class SP:
    count = 0
    def __init__(self , Id ,TenSP, DonGia) :
        self.TenSP = TenSP
        self.DonGia = DonGia
        self.Id = Id
        SP.count = SP.count + 1

    def set_TenSP(self, TenSP):
        self.TenSP = TenSP

    def set_DonGia(self, DonGia):
        self.DonGia = DonGia
    
    def set_Id(self, Id):
        self.Id = Id

    def get_Id(self):
        return self.Id

    def get_TenSP(self):
        return self.TenSP

    def get_DonGia(self):
        return self.DonGia

    def show_SP(self):
        print(self.Id, ". ", self.TenSP, "(" , self.DonGia, "VND)")

    

    