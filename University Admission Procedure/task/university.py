application_list = """Jermine Brunton 3.71 Physics Engineering Mathematics
Justo Mirfin 3.14 Engineering Biotech Chemistry
Uzma Naysmythe 3.28 Chemistry Engineering Mathematics
Koury Wingo 3.51 Engineering Biotech Mathematics
Kentrell Hillhouse 2.58 Mathematics Engineering Biotech
Trica Macalpine 3.90 Engineering Mathematics Biotech
Sang Muldoon 3.42 Physics Mathematics Engineering
Laney Braithwaite 3.81 Physics Chemistry Mathematics
Spring Burridge 3.55 Mathematics Chemistry Engineering
Delta Fanny 2.62 Chemistry Physics Mathematics
Elen Ashbury 3.28 Mathematics Chemistry Biotech
Ruthanne Scaife 3.79 Engineering Biotech Mathematics
Jaemi Hallets 3.61 Physics Engineering Mathematics
Artavious Fay 3.05 Engineering Biotech Chemistry
Franki Dinnis 3.21 Chemistry Biotech Mathematics
Marlynn Favell 3.81 Engineering Biotech Mathematics
Sameera Procter-Baines 3.18 Mathematics Engineering Biotech
Shantale Tompkins 3.90 Engineering Mathematics Biotech
Cornellius Turney 3.22 Physics Mathematics Engineering
Blia Sagar 3.44 Physics Chemistry Biotech
Wynn Crampton 3.51 Mathematics Chemistry Engineering
Linda Risley 3.22 Chemistry Physics Mathematics
Divina Butterworth 3.27 Mathematics Chemistry Biotech
Meshell Otway-Ruthven 3.89 Engineering Biotech Mathematics
Ammon Janssen 3.16 Physics Engineering Mathematics
Maila Greg 3.14 Mathematics Biotech Chemistry
Madiha Milligan 3.25 Physics Engineering Chemistry
Humphrey Spakeman 3.44 Chemistry Biotech Mathematics
Marygrace Wheelton 3.58 Mathematics Engineering Biotech
Takyra Sieminski 3.97 Engineering Mathematics Physics
Jathan Birley 3.42 Physics Mathematics Engineering
Tawnia Alcock 3.60 Biotech Chemistry Physics
Quinisha Clarkson 3.52 Mathematics Chemistry Engineering
Dashanna Herron 3.12 Physics Chemistry Mathematics
Verlon Mcconnell 3.28 Mathematics Chemistry Biotech
Tawsha Rodgers 3.79 Engineering Biotech Mathematics
Derick Whatley 3.61 Physics Engineering Mathematics
Tisheena Mckenney 3.18 Engineering Physics Biotech
Kyona Catrol 3.25 Chemistry Biotech Mathematics
Jamarl Delap 3.11 Engineering Biotech Mathematics
Tulio Carloss 3.18 Mathematics Engineering Physics
Kaylie Lanthis 3.22 Engineering Mathematics Biotech
Martha Hatchard 3.22 Physics Mathematics Engineering
Genee Mccrae 3.41 Biotech Chemistry Physics
Luna Pheobe 3.55 Chemistry Mathematics Engineering
Savvas Hjellstrom 2.77 Chemistry Biotech Mathematics
Mehul Bull 3.21 Mathematics Physics Biotech
Kennedy Barrett 3.90 Chemistry Biotech Mathematics
Marquita Mcrae 3.51 Physics Engineering Biotech
Natha Keefe 3.14 Engineering Biotech Chemistry
Crescentia Dow 3.79 Chemistry Physics Mathematics
Randon Bradhust 3.68 Biotech Engineering Chemistry
Dashawn Bosley 3.54 Mathematics Chemistry Biotech
Nicolasa Sumpter 3.82 Engineering Mathematics Biotech
Cressie Gillespie 3.10 Physics Mathematics Engineering
Tawny Crockett 3.01 Chemistry Biotech Physics
Kennon Inverarity 3.50 Mathematics Engineering Chemistry
Halima Brydone 3.72 Chemistry Physics Mathematics
Esther Bratby 2.67 Mathematics Chemistry Biotech
Lorry Bunger 3.79 Engineering Biotech Physics
Fatemah Desavigny 3.00 Physics Mathematics Engineering
Marti Mclaws 3.05 Engineering Chemistry Biotech
Estephanie Phelps 3.21 Chemistry Physics Mathematics
Tommi Peerless 3.85 Engineering Physics Mathematics
Cynthia Hermitton 3.10 Engineering Biotech Chemistry
Cheyla Hankinson 3.82 Engineering Mathematics Biotech
Giovanna Keel 3.25 Physics Mathematics Engineering
Narissa Worthington 3.30 Biotech Chemistry Mathematics
Aundria Guthrie 3.51 Mathematics Chemistry Engineering
Teneil Maclean 3.22 Mathematics Physics Chemistry
Shealynn Melville 3.02 Mathematics Chemistry Physics
Darrah Smyth 3.89 Physics Biotech Engineering
Elroy Leyte 3.16 Engineering Physics Mathematics
Jessye Allum 3.14 Mathematics Biotech Chemistry
Pearl Pullins 3.25 Chemistry Engineering Mathematics
Brittania Denny 3.71 Chemistry Physics Mathematics
Mendy Macmillan 3.38 Biotech Engineering Mathematics
Ramina Ogilvie 3.18 Mathematics Engineering Biotech
Ronel Cowan 3.80 Engineering Mathematics Biotech
Stacey Revill 3.92 Chemistry Physics Mathematics
Mir Ashley 3.52 Mathematics Physics Chemistry
Ayeshia Jackman 3.12 Chemistry Physics Mathematics
Jordann Rives 3.28 Mathematics Chemistry Biotech
Katrine Proby 3.77 Engineering Biotech Mathematics
Jermain Stobbs 3.61 Physics Engineering Mathematics
Sharief Macallister 3.18 Engineering Physics Biotech
Shannette Cowie 3.25 Chemistry Biotech Mathematics
Melena Hearn 3.11 Engineering Biotech Mathematics
Moraima Kendell 3.18 Mathematics Engineering Physics
Amira Giddings 3.22 Engineering Mathematics Physics
Tyrone Fern 3.00 Physics Mathematics Engineering
Joaquin Mytton 3.28 Mathematics Chemistry Biotech
Ehab Cocciardi 3.70 Engineering Biotech Mathematics
Tamkia Fish 3.64 Physics Engineering Mathematics
Deniz Blanchard 3.05 Engineering Biotech Chemistry
Mira Riley 3.11 Chemistry Biotech Mathematics
Loura Macansh 3.01 Engineering Physics Mathematics
Nastassja Trustram 3.77 Mathematics Engineering Physics"""


class University:
    departments = ["Biotech", "Chemistry", "Engineering", "Mathematics", "Physics"]

    def __init__(self, accept_num):
        self.accept_num = accept_num
        self.applicants = []
        self.departments_students = {}

    def get_applicants_list(self):
        with open("applicants.txt", "r") as applicants_file:
            applicants = applicants_file.readlines()
        # applicants = application_list.split("\n")

        self.applicants = [apt.strip("\n").split() for apt in applicants]
        self.applicants.sort(key=lambda x: (-float(x[2]), x[0], x[1]))
        # print(self.applicants)

    def accept_students(self, rank):
        accepted = []
        for x in self.applicants:
            if not self.departments_students.get(x[rank + 3]) or len(self.departments_students[x[rank + 3]]) < self.accept_num:
                self.departments_students.setdefault(x[rank + 3], []).append(x)
                accepted.append(x)
        for x in accepted:
            self.applicants.remove(x)

    def display_admission(self):
        for dpt in self.departments:
            self.departments_students[dpt].sort(key=lambda x: (-float(x[2]), x[0], x[1]))
            print(dpt)
            for student in self.departments_students[dpt]:
                print(f"{student[0]} {student[1]} {student[2]}")


university = University(int(input()))
university.get_applicants_list()
for rk in range(3):
    university.accept_students(rk)
university.display_admission()
