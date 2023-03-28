pada file minggu ke-3 berisi tentang hal untuk melakukan Sturktur Data

Tipe data daftar memiliki beberapa metode lagi. Berikut ini semua metode objek daftar:

list.append ( x )
digunakan untuk menambahkan item ke akhir daftar. Setara dengan .a[len(a):] = [x]

list.extend(iterable) ( dapat diubah )
digunakan untuk perpanjang daftar dengan menambahkan semua item dari iterable. Setara dengan .a[len(a):] = iterable

list.insert ( i , x )
digunakan untuk masukkan item pada posisi tertentu. Argumen pertama adalah indeks elemen sebelum disisipkan, jadi sisipkan di bagian depan daftar, dan sama dengan .a.insert(0, x)a.insert(len(a), x)a.append(x)

list.remove ( x )
digunakan untuk menghapus item pertama dari daftar yang nilainya sama dengan x . Itu memunculkan ValueErrorjika tidak ada item seperti itu.

daftar. pop ( [ i ] )
unutk menghapus item pada posisi yang diberikan dalam daftar, dan kembalikan. Jika tidak ada indeks yang ditentukan, a.pop()hapus dan kembalikan item terakhir dalam daftar. (Kurung siku di sekitar i pada tanda tangan metode menunjukkan bahwa parameternya opsional, bukan berarti Anda harus mengetikkan tanda kurung siku pada posisi itu. Anda akan sering melihat notasi ini di Referensi Pustaka Python.)

list.clear ( )
figunakan untuk menghapus semua item dari daftar. Setara dengan .del a[:]

daftar. indeks ( x [ , awal [ , akhir ] ] )
digunakan untuk membalikan indeks berbasis nol dalam daftar item pertama yang nilainya sama dengan x . Menaikkan a ValueErrorjika tidak ada item seperti itu.

Argumen opsional awal dan akhir diinterpretasikan seperti dalam notasi irisan dan digunakan untuk membatasi pencarian ke urutan tertentu dari daftar. Indeks yang dikembalikan dihitung relatif terhadap awal urutan penuh daripada argumen awal .

list.count ( x )
digunakan untuk membalikan berapa kali x muncul dalam daftar.

list.sort(*, key=None, reverse=False)
digunakan untuk melakukan Sortir item daftar pada tempatnya (argumen dapat digunakan untuk mengurutkan kustomisasi, lihat sorted()penjelasannya).

list.reverse()( )
digunakan untuk membalikkan elemen daftar pada tempatnya.

list.copy()
untuk mengembalikan salinan daftar yang dangkal. Setara dengan a[:].
