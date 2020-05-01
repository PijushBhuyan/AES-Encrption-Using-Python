# AES Encryption in Python
A simple GUI implementation of 128 bit AES Rjindael encryption (single round till now) in Python
	<p align=center><img width="620"  height="326"  src="https://in.mathworks.com/matlabcentral/mlc-downloads/downloads/649c6929-37cf-4d50-b545-af9a11396bf4/93de5ae7-ecb0-4776-84a1-3974dd921805/images/screenshot.jpg"> </p>

### Dependencies - 
* **Numpy**  - _Python's Array Processing Library_
* **Tinkter** - _Python's GUI Library_
* **Pillow** -  _Python's Image Processing Library_
### Installing Dependencies -
1. Install PIP (_Python Package Installer_)   - 
     * `` sudo apt update``
     * ``sudo apt install python3-pip``
     * ``pip3 --version``
2. Numpy -
	*  ``pip3 install numpy``
3. Pillow - 
	* ``pip3 install Pillow``
4. Tkinter - 
	* ``sudo apt-get install python-tk``

## Encryption Algorithm - 

A typical AES encryption algorithm runs for 10 rounds -each round comprising of 4 processes.The 1st round is shown below - 


![First Round Process](https://www.tutorialspoint.com/cryptography/images/first_round_process.jpg)


<p>Note - We have restricted our algorithm to a single round for the sake of simplicity.
	
### Byte Substitution (SubBytes)

The 16 input bytes are substituted by looking up a fixed table (S-box) given in design. 


![sub bytes](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/AES-SubBytes.svg/320px-AES-SubBytes.svg.png)


### Shiftrows

Each of the four rows of the matrix is shifted to the left. Any entries that ‘fall off’ are re-inserted on the right side of row. Shift is carried out as follows −

-   First row is not shifted.
    
-   Second row is shifted one (byte) position to the left.
    
-   Third row is shifted two positions to the left.
    
-   Fourth row is shifted three positions to the left.
    
-   The result is a new matrix consisting of the same 16 bytes but shifted with respect to each other.
  
    <img width="400"  height="144"  src="https://upload.wikimedia.org/wikipedia/commons/e/e3/AES-ShiftRows.png">


### MixColumns

Each column of four bytes is now transformed using a special mathematical function. This function takes as input the four bytes of one column and outputs four completely new bytes, which replace the original column. The result is another new matrix consisting of 16 new bytes. We have used the Galois Field Lookup tables for the sake of simplicity.

<img width="400"  height="206"  src="https://upload.wikimedia.org/wikipedia/commons/9/99/AES-MixColumns.png">

### Addroundkey
<img width="320"  height="249"  src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/AES-AddRoundKey.svg/320px-AES-AddRoundKey.svg.png">

The 16 bytes of the matrix are now considered as 128 bits and are XORed to the 128 bits of the round key. If this is the last round then the output is the ciphertext. Otherwise, the resulting 128 bits are interpreted as 16 bytes and we begin another similar round.


## Decryption Algorithm -

The process of decryption of an AES ciphertext is similar to the encryption process in the reverse order. Each round consists of the four processes conducted in the reverse order −

-   Add round key
-   Mix columns
-   Shift rows
-   Byte substitution



## How to use :
### Encryption - 
1. Run the gui.py script to start the application
2. Select the **encrypt** tab
3. Enter the text you want to encrpyt. You can also select a txt file that contains the text to be encrypted
4. Enter a 16 character key (make sure to remember this otherwise you wont be able to decrypt later on)
5. Enter the name of the file you wish to be saved without any extensions
6. Click encrypt. it will be saved as txt fille in the **Encrypted** folder

### Decryption - 
1. Select the **decrypt** tab 
2. Enter the name of the encypted file (no need to worry about the relative path,just enter file name without extension)
3. Enter the 16 character key used for encryption
4. Click decrypt. it will be saved in the **Decrypted**  folder as a txt file. 

## Screenshots - 
### Encryption -
<img src = "Screenshots/encryption 1.png">
<img src = "Screenshots/encryption 2.png">
<img src = "Screenshots/encryption 3.png">

### Decryption - 
<img src = "Screenshots/decryption 1.png">
<img src = "Screenshots/decryption 2.png">
<img src = "Screenshots/decryption 3.png">


