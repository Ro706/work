{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOwEMXiIjPDYEWKyd5kSGxY",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Ro706/work/blob/main/colab.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Bxb2KgPtzreg",
        "outputId": "0c620574-7e6a-49be-94d5-5b19781d4dae"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "RoHit\n",
            "<class 'str'>\n",
            "5\n",
            "140709337775664\n",
            "ROHIT\n",
            "rohit\n",
            "\n",
            "enter value:12345678990\n",
            "['1', '2', '3', '4', '5', '6', '7', '8', '9', '9', '0']\n",
            "11\n",
            "1\n",
            "2\n",
            "3\n",
            "4\n",
            "5\n",
            "6\n",
            "7\n",
            "8\n",
            "9\n",
            "9\n",
            "0\n",
            "1 2 rohit\n",
            "False\n",
            "True\n",
            "5\n"
          ]
        }
      ],
      "source": [
        "\n",
        "# day 1 python class\n",
        "a = \"RoHit\" # value of 'a' is aditya\n",
        "s,b,c=1,2,\"rohit\" #value of 's','b','c' is 1,2,\"rohit\"\n",
        "a\n",
        "print(a) #printing value 'a'\n",
        "print(type(a))#printing value datatype\n",
        "print(len(a))#printing lengthof the variable 'a'\n",
        "print(id(a))#printing id or you can say that printing storage location of varial 'a'\n",
        "print(a.upper())#printing  variable 'a' upper value\n",
        "print(a.lower())#printing variable 'a' lower value\n",
        "print()\n",
        "list1=list(input(\"enter value:\"))\n",
        "print(list1)\n",
        "print(len(list1))\n",
        "for i in list1:\n",
        "    print(i)\n",
        "print(s,b,c)#printing multiple values\n",
        "print(isinstance(a,int))\n",
        "print(isinstance(b,int))\n",
        "a = \"rohit\"\n",
        "n = len(a)\n",
        "print(n)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#day 2 python class\n",
        "x = str(3)\n",
        "print(type(x))\n",
        "y = int(3)\n",
        "print(type(y))\n",
        "y = float(3)\n",
        "print(x)\n",
        "print(y)\n",
        "print(type(y))\n",
        "c =0b100 #for binary number system\n",
        "print(type(c))\n",
        "print(c)\n",
        "print(int(\"300\",5))\n",
        "print(int(\"1010\",2))\n",
        "print(int(\"12120\",3))\n",
        "print(int(\"1111111\",2))\n",
        "print(int(\"66226\",7))\n",
        "print(int(\"6622611\",32))\n",
        "a = 0b1010 #binary\n",
        "b = 0o170 #octal\n",
        "print(a,b)\n",
        "h = 2+3.14j #complex literal\n",
        "print(h)\n",
        "print(complex(3+84))\n",
        "print (u'\\u00dc \\n nic\\n')\n",
        "print('Omega: \\u03A9')\n",
        "name = \"rohit\"\n",
        "classes = \"12/G\"\n",
        "adress=\"sec -4 G qno-241\"\n",
        "print(name,classes,adress)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BKpzoQz8NJ_E",
        "outputId": "8a7cf991-eeea-43f4-dde3-75398833d821"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'str'>\n",
            "<class 'int'>\n",
            "3\n",
            "3.0\n",
            "<class 'float'>\n",
            "<class 'int'>\n",
            "4\n",
            "75\n",
            "10\n",
            "150\n",
            "127\n",
            "16582\n",
            "6645946401\n",
            "10 120\n",
            "(2+3.14j)\n",
            "(87+0j)\n",
            "Ü \n",
            " nic\n",
            "\n",
            "Omega: Ω\n",
            "rohit 12/G sec -4 G qno-241\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#my work\n",
        "num= int(input(\"enter any four digit number:\"))\n",
        "sum=0\n",
        "for i in str(num):\n",
        "    sum += int(i)\n",
        "print (sum)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RR7xgQYtPbjA",
        "outputId": "f5c5e34a-2974-4dd6-f25d-f6ba543bbe5a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter any four digit number:5555\n",
            "20\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#day 3 python class\n",
        "print(ord(\"h\"))\n",
        "print(chr(122))\n",
        "print(int(0x00dc))\n",
        "print(int(0x012dc))\n",
        "a = True\n",
        "b = False\n",
        "print(a + 100, b+100)\n",
        "str_my = \"sparshm\"\n",
        "print(str_my [1])\n",
        "print(str_my[-1])\n",
        "print(str_my[1:4])\n",
        "print(str_my[0:5:2])\n",
        "print(str_my[5:0:-1])\n",
        "print(str_my[::2])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MAleG-JBHUbq",
        "outputId": "d8e691c2-649c-4502-c4d1-88f9e3ace7c6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "104\n",
            "z\n",
            "220\n",
            "4828\n",
            "101 100\n",
            "p\n",
            "m\n",
            "par\n",
            "sas\n",
            "hsrap\n",
            "sasm\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#write a program to declare a string consisting  of all digits from 0-9 print all,odd,and even digits from the string\n",
        "my_str = \"0123456789\"\n",
        "print(my_str)\n",
        "print(my_str[::2])#even\n",
        "print(my_str[1:10:2])#odd\n",
        "m_s = \"sitnagpur\"\n",
        "print(m_s[-3:-5:-1])\n",
        "print(m_s[5:2:-1])\n",
        "#write a program to add two number\n",
        "a = 3\n",
        "b = 4\n",
        "c = a+b\n",
        "print(c)\n",
        "#write a program to  input form user\n",
        "username = str(input(\"please enter your name:\"))\n",
        "print(\"hello \",username)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hd80wMbpOZoJ",
        "outputId": "46a34d6c-371d-4330-f123-2cb1db59dbcc"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0123456789\n",
            "02468\n",
            "13579\n",
            "pg\n",
            "gan\n",
            "7\n",
            "please enter your name:rohit\n",
            "hello  rohit\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#day 4 python class\n",
        "my_str=\"rohit mandal\"\n",
        "s1 = my_str.split()\n",
        "s2 = my_str.split(sep = \" \")\n",
        "print(s1,s2)\n",
        "my_str = \"rohitmandal\"\n",
        "s1 = my_str.split(sep = \"a\")\n",
        "print(s1)\n",
        "name = input(\"enter your name: \")\n",
        "print(\"hello\",name)\n",
        "print(type(name))\n",
        "name = input(\"enter your name:\")\n",
        "print(\"Hello\",name.upper())\n",
        "print(\"hello \",name.title())\n",
        "y,x= input(\"enter two naumber: \").split()\n",
        "print(int(x)+int(y))\n",
        "#real number and perform it multplication\n",
        "real1 = float(input(\"enter your real number1: \"))\n",
        "real2 = float(input(\"enter your real number2: \"))\n",
        "print(real1*real2)\n",
        "#wap to get your name as input and print ascii value \n",
        "name = input(\"enter your name: \")\n",
        "a = len(name)\n",
        "print(\"name len =\", a)\n",
        "for i in range(int(a)):\n",
        "    print(ord(name[i]))\n",
        "print(\"thank you\")  "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4-6xk45zODkZ",
        "outputId": "2b3c44fe-00f3-49bf-eb0b-2041d286380e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['rohit', 'mandal'] ['rohit', 'mandal']\n",
            "['rohit', 'mandal']\n",
            "enter your name: rohit\n",
            "hello rohit\n",
            "<class 'str'>\n",
            "enter your name:rohit kumar mandal\n",
            "Hello ROHIT KUMAR MANDAL\n",
            "hello  Rohit Kumar Mandal\n",
            "enter two naumber: 1 2\n",
            "3\n",
            "enter your real number1: 112\n",
            "enter your real number2: 12.22\n",
            "1368.64\n",
            "enter your name: rohit\n",
            "name len = 5\n",
            "114\n",
            "111\n",
            "104\n",
            "105\n",
            "116\n",
            "thank you\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "name = input(\"enter your name: \")\n",
        "a = len(name)\n",
        "print(\"name len =\", a)\n",
        "for i in range(int(a)):\n",
        "    print(ord(name[i]))\n",
        "print(\"thank you\")    \n",
        "\n",
        "    \n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WIXiqdGDcv3y",
        "outputId": "ad030083-2496-41a9-e200-e06603804ba2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter your name: rohit\n",
            "name len = 5\n",
            "114\n",
            "111\n",
            "104\n",
            "105\n",
            "116\n",
            "thank you\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "ro706 = \"hello rohit\"\n",
        "num = 100\n",
        "text = \"%s your marks: %d\"%(ro706,num)\n",
        "print(text)\n",
        "morpheus7104 = \"chutiya\"\n",
        "yu = 111\n",
        "xxx = \"%s is not : %d\"%(morpheus7104,yu)\n",
        "print(xxx)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LZ8yCgdzmCe_",
        "outputId": "ca336f7c-16c7-48ae-81e5-ca05f8de278f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "hello rohit your marks: 100\n",
            "chutiya is not : 111\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#home work\n",
        "str_my = input(\"enter your name:\")\n",
        "print(str_my.isalpha())\n",
        "print(str_my[0].isalpha())\n",
        "print(str_my.isdigit())#1\n",
        "print(str_my.isidentifier())#2\n",
        "print(str_my.islower())#3\n",
        "print(str_my.title().istitle())#4\n",
        "print(str_my.istitle())#5\n",
        "table = {110:97,122:98,117:None}\n",
        "print(str_my.translate(table))#6\n",
        "print(str_my.swapcase())#7\n",
        "print(str_my.casefold())#8\n",
        "print(str_my.capitalize())#9\n",
        "print(str_my.endswith(\"mandal\"))#10\n",
        "print(str_my.startswith(\"rohit\"))#11\n",
        "print(str_my.zfill(7))#12\n",
        "list1 =[1,2,3,4]\n",
        "print(list1.index(2))#13\n",
        "print(str_my.find(\"k\"))#14\n",
        "print(str_my.count(\"rohit\"))#15\n",
        "print(str_my.rfind(\"o\"))#16\n",
        "print(str_my.encode())#17\n",
        "print(str_my.center(23))#18\n",
        "print(str_my.center(20))#19\n",
        "print(str_my.isdecimal())#20\n",
        "print(str_my.isnumeric())#21"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qV5D70LgF01C",
        "outputId": "1bc36b46-7674-4be0-dee7-765b16bdcc92"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter your name:rohit\n",
            "True\n",
            "True\n",
            "False\n",
            "True\n",
            "True\n",
            "True\n",
            "False\n",
            "rohit\n",
            "ROHIT\n",
            "rohit\n",
            "Rohit\n",
            "False\n",
            "True\n",
            "00rohit\n",
            "1\n",
            "-1\n",
            "1\n",
            "1\n",
            "b'rohit'\n",
            "         rohit         \n",
            "       rohit        \n",
            "False\n",
            "False\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#list \n",
        "list1 =list(input(\"enter your letter list:\"))\n",
        "print(list1)\n",
        "print(list1[1])\n",
        "n = 0\n",
        "for i in list1:\n",
        "    print(list1[n])\n",
        "    n +=1"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "37I-ToAMMt2V",
        "outputId": "efd38a60-8249-40b2-940d-9f512e229dca"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter your letter list:rohit\n",
            "['r', 'o', 'h', 'i', 't']\n",
            "o\n",
            "r\n",
            "o\n",
            "h\n",
            "i\n",
            "t\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(00,100,2):\n",
        "    print(i)\n",
        "    if i  == 28:\n",
        "      print(\"nice\")\n",
        "      break\n",
        "    else:\n",
        "      pass  "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "StSdSIV6P6FO",
        "outputId": "29e34a2f-75e2-4da4-a8d5-21881ec3bcaa"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0\n",
            "2\n",
            "4\n",
            "6\n",
            "8\n",
            "10\n",
            "12\n",
            "14\n",
            "16\n",
            "18\n",
            "20\n",
            "22\n",
            "24\n",
            "26\n",
            "28\n",
            "nice\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']\n",
        "print(months[6],\"\\n\")\n",
        "print(months[6:9],\"\\n\")\n",
        "print(months[0:11:2],\"\\n\")\n",
        "print(months[-12:-1])\n",
        "print(months[-12:-1])\n",
        "print(months[12:1:-1])\n",
        "print(months[12:5:-1])\n",
        "print(months[12:3:-1])\n",
        "print(months[-1:-5:-1])\n",
        "print(months[-12:-8:1],\"\\n\")\n",
        "list1=list(range(-4,10,2))\n",
        "print(\"list1=\",list1)\n",
        "list2 =list(range(-6,6,1))\n",
        "print(\"list2\",list2)\n",
        "print(list1+list2)\n",
        "print(list2 * 2)\n",
        "print(list1 in list2)\n",
        "print(list1 not in list2 )\n",
        "n = 0\n",
        "list1.append(1)\n",
        "print(list1)\n",
        "list1.insert(0,11) #insert(indexnumber,element name or number)\n",
        "print(\"list1 =\",list1)\n",
        "l=list1.sort()\n",
        "print(sorted(list1,reverse=True))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rIv6WafL4nty",
        "outputId": "3d7445db-f4d9-4026-ca4d-e98a4fad91f0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "July \n",
            "\n",
            "['July', 'August', 'September'] \n",
            "\n",
            "['January', 'March', 'May', 'July', 'September', 'November'] \n",
            "\n",
            "['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November']\n",
            "['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November']\n",
            "['December', 'November', 'October', 'September', 'August', 'July', 'June', 'May', 'April', 'March']\n",
            "['December', 'November', 'October', 'September', 'August', 'July']\n",
            "['December', 'November', 'October', 'September', 'August', 'July', 'June', 'May']\n",
            "['December', 'November', 'October', 'September']\n",
            "['January', 'February', 'March', 'April'] \n",
            "\n",
            "list1= [-4, -2, 0, 2, 4, 6, 8]\n",
            "list2 [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]\n",
            "[-4, -2, 0, 2, 4, 6, 8, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]\n",
            "[-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]\n",
            "False\n",
            "True\n",
            "[-4, -2, 0, 2, 4, 6, 8, 1]\n",
            "list1 = [11, -4, -2, 0, 2, 4, 6, 8, 1]\n",
            "[11, 8, 6, 4, 2, 1, 0, -2, -4]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#to find the sum of 5 digit number\n",
        "a = []\n",
        "a.append(int(input(\"enter number 1:\")))\n",
        "a.append(int(input(\"enter number 2:\")))\n",
        "a.append(int(input(\"enter number 3:\")))\n",
        "a.append(int(input(\"enter number 4:\")))\n",
        "a.append(int(input(\"enter number 5:\")))\n",
        "sum = a[0]+a[1]+a[2]+a[3]+a[4]\n",
        "print(\"sum=\",sum)"
      ],
      "metadata": {
        "id": "GHNTdapd5PaM",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "ca3bbed9-6501-4544-d7c9-d2d8b326ed06"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter number 1:1\n",
            "enter number 2:2\n",
            "enter number 3:3\n",
            "enter number 4:4\n",
            "enter number 5:5\n",
            "sum= 15\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#1)to find the sum of 5 digit number\n",
        "#2)to find weather arm is or not\n",
        "#1)\n",
        "a = b = int(input(\"enter any 5 digit number:\"))\n",
        "b = a%10\n",
        "a = a//10\n",
        "b1 = a%10\n",
        "a = a//10\n",
        "b2 = a%10\n",
        "a = a//10\n",
        "b3 = a%10\n",
        "a = a//10\n",
        "b4 = a%10\n",
        "a =  a//10\n",
        "print(b,b1,b2,b3,b4)\n",
        "print('sum',b+b1+b2+b3+b4)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WGoFwn-Qcas6",
        "outputId": "d8369b03-cae1-4a68-cacf-f2599f183b18"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter any 5 digit number:12345\n",
            "5 4 3 2 1\n",
            "sum 15\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a = b = int(input(\"enter any 3 digit number:\"))\n",
        "b = a%10\n",
        "a = a//10\n",
        "b1 = a%10\n",
        "a = a//10\n",
        "b2 = a%10\n",
        "print(b**3+b1**3+b2**3)\n",
        "print('armstrong number')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ntf14wK_0IOS",
        "outputId": "fc6031ad-12f0-4d00-8ccd-c58b016fcb4e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter any 3 digit number:153\n",
            "153\n",
            "armstrong number\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "num = int(input(\"enter number:\"))\n",
        "ans = 0\n",
        "digits = len(str(num))\n",
        "dup_number = num\n",
        "while (dup_number != 0):\n",
        "    remainder = dup_number % 10\n",
        "    ans = ans + remainder**digits\n",
        "    dup_number = dup_number//10\n",
        "if(num == ans):\n",
        "    print(num, \"is Armstrong number\")\n",
        "else:\n",
        "    print(num, \"is not Armstrong number\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Q81CUWV771cs",
        "outputId": "d81232fa-bb85-4414-8563-23a671247c21"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter number:1234\n",
            "1234 is not Armstrong number\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#day 6 python class\n",
        "list1= [\"CAT\",\"DOG\",\"TIGER\",\"JAK\",\"apple\"]\n",
        "print(sorted(list1,key=str.lower))\n",
        "list1 =[[1,2,3,4],[\"rohit\",\"riya\",\"raj\",\"khushi\"],[36,37,32,33]]\n",
        "print(list1)\n",
        "print(\"list1 =\",list1[0],\"list2=\",list1[1],\"list3=\",list1[2])\n",
        "print(list1[0:3][0:3])\n",
        "#tuple\n",
        "t =(1,2,3,4,\"three\")\n",
        "print(t)\n",
        "print(type(t))\n",
        "t = (1,2,3,4,5)\n",
        "a,b,c,d,e = t\n",
        "print(a,b,c,d)\n",
        "for i in t:\n",
        "    print(i)\n",
        "del t\n",
        "print(\"tuple is deleted successfully\")\n",
        "t = (\"21-06-2004\",[\"rohit\",\"sager\"])\n",
        "r = (\"21-06-2004\",[\"rohit\",\"sager\"])\n",
        "print(r == t)\n",
        "print(id(r),id(t))\n",
        "print(t is r)\n",
        "t = r\n",
        "print(r == t)\n",
        "print(id(r),id(t))\n",
        "print(t is r)\n",
        "list1 = t[1]\n",
        "list1.append(\"ro706\")\n",
        "print(t)\n",
        "'''t[1]=[1,2,3]\n",
        "print(t)'''\n",
        "set1 = {1,2,3,4}\n",
        "print(set1) \n",
        "set1.add(0)\n",
        "set1.update([10,11,12,13])\n",
        "print(set1)\n",
        "set1.pop()\n",
        "#set1.clear()\n",
        "print(set1)\n",
        "set1.remove(10)\n",
        "print(set1)\n",
        "set1.discard(0)\n",
        "set2 = {1,2,3,0,10}\n",
        "print(set2)"
      ],
      "metadata": {
        "id": "0DxmoX94Vtbn",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "b4d3c961-a6fd-4b93-ffcc-80ce4f5d4b42"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['apple', 'CAT', 'DOG', 'JAK', 'TIGER']\n",
            "[[1, 2, 3, 4], ['rohit', 'riya', 'raj', 'khushi'], [36, 37, 32, 33]]\n",
            "list1 = [1, 2, 3, 4] list2= ['rohit', 'riya', 'raj', 'khushi'] list3= [36, 37, 32, 33]\n",
            "[[1, 2, 3, 4], ['rohit', 'riya', 'raj', 'khushi'], [36, 37, 32, 33]]\n",
            "(1, 2, 3, 4, 'three')\n",
            "<class 'tuple'>\n",
            "1 2 3 4\n",
            "1\n",
            "2\n",
            "3\n",
            "4\n",
            "5\n",
            "tuple is deleted successfully\n",
            "True\n",
            "140707458691872 140707458437760\n",
            "False\n",
            "True\n",
            "140707458691872 140707458691872\n",
            "True\n",
            "('21-06-2004', ['rohit', 'sager', 'ro706'])\n",
            "{1, 2, 3, 4}\n",
            "{0, 1, 2, 3, 4, 10, 11, 12, 13}\n",
            "{1, 2, 3, 4, 10, 11, 12, 13}\n",
            "{1, 2, 3, 4, 11, 12, 13}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "set1 = {1,2,3,4}\n",
        "a= (1.0,(1,2,3),\"hello\")\n",
        "set2=a\n",
        "print(set1)\n",
        "print(set2)"
      ],
      "metadata": {
        "id": "vGxJnxhrYvzs",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "fc82e054-65ef-44f2-aabe-30935ca61716"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{1, 2, 3, 4}\n",
            "(1.0, (1, 2, 3), 'hello')\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "t1 = ()\n",
        "t2 = (1,2,3)\n",
        "t3 = (1,\"hello\",34)\n",
        "print(t1)\n",
        "print(t2)\n",
        "print(t3)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6142k1jCfFoY",
        "outputId": "9051cf61-d6c3-43b0-845e-fd1f0c405f51"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "()\n",
            "(1, 2, 3)\n",
            "(1, 'hello', 34)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "t1 = (3,46,\"cat\")\n",
        "print(t1)\n",
        "print(t1[0])\n",
        "print(t1[1])\n",
        "print(t1[2])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KNyDZ1hDhMRP",
        "outputId": "5900072a-6fe8-473e-97f8-1072d2195106"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "(3, 46, 'cat')\n",
            "3\n",
            "46\n",
            "cat\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "tuple1 = (0,1,2,3)\n",
        "tuple2 = (\"SIT\",\"Nagpur\")\n",
        "tuple3 = tuple1 + tuple2\n",
        "print(\"tuple1 \\n\",tuple1) \n",
        "print(\"tuple2 \\n\",tuple2)\n",
        "print(\"tuple after concetnation \\n\",tuple3) "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2Bx3_rB6hdvr",
        "outputId": "286d72ce-7422-4f06-8b02-2a253b41755c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "tuple1 \n",
            " (0, 1, 2, 3)\n",
            "tuple2 \n",
            " ('SIT', 'Nagpur')\n",
            "tuple after concetnation \n",
            " (0, 1, 2, 3, 'SIT', 'Nagpur')\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "classroll = {\"rohit\":7,\"aditya\":24,\"nishant\":61,\"anmol\":23,\"devanshu\":22}\n",
        "print(classroll)\n",
        "classroll['rohit']=75\n",
        "classroll['aditya'] = 92\n",
        "classroll[\"nishant\"]=125\n",
        "classroll['anmol'] = 91\n",
        "classroll['devanshu'] = 90\n",
        "print(classroll)\n",
        "print(classroll.keys())\n",
        "print(classroll.values())\n",
        "print(type(classroll))\n",
        "print(1,2,3,4)\n",
        "print(1,2,3,4, sep =\"#\" ,end=\"$\")\n",
        "print(1,2,3,4, sep =' ',end =\"\\n\")\n",
        "print(1,2,3,4, sep =\"@\",end=\"$\",flush = True)\n",
        "print(\"\")\n",
        "print(\"     *\",\"    * *\",\"   * * *\",\"  * * * *\",sep =\"\\n\",end =\"\")"
      ],
      "metadata": {
        "id": "wiiQNAgBjcYE",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "739f9d11-4267-4a9f-e12e-9d35d9097f0f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'rohit': 7, 'aditya': 24, 'nishant': 61, 'anmol': 23, 'devanshu': 22}\n",
            "{'rohit': 75, 'aditya': 92, 'nishant': 125, 'anmol': 91, 'devanshu': 90}\n",
            "dict_keys(['rohit', 'aditya', 'nishant', 'anmol', 'devanshu'])\n",
            "dict_values([75, 92, 125, 91, 90])\n",
            "<class 'dict'>\n",
            "1 2 3 4\n",
            "1#2#3#4$1 2 3 4\n",
            "1@2@3@4$\n",
            "     *\n",
            "    * *\n",
            "   * * *\n",
            "  * * * *"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#python class 8\n",
        "x = 23\n",
        "y = 82\n",
        "print(\"two value are {1} and {0}\".format(x,y))\n",
        "print(f\"two value are {x} and {y}\")\n",
        "''' \n",
        "arithmatic oprators : +,-,/,*,%,//,**[BODMAS]\n",
        "comparison oprators : <,>,==,,!=,>=,<=\n",
        "logical oprators : and ,or,not\n",
        "bitwise oprator : !,&,~,^,>>,<<\n",
        "'''\n",
        "print(5<<3)\n",
        "print(10 >> 2)\n",
        "print(5&6)\n",
        "letter = input('enter character:')\n",
        "print('vowel') if letter in 'aeiou'else print('no vowel')"
      ],
      "metadata": {
        "id": "-L4lA_NFqfgE",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "c6181754-934f-4a77-a743-1e93f9853570"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "two value are 82 and 23\n",
            "two value are 23 and 82\n",
            "40\n",
            "2\n",
            "4\n",
            "enter character:a\n",
            "vowel\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#wap to check weather enter number is even or odd by using bitwise\n",
        "num = int(input(\"enter num:\"))\n",
        "print('odd') if num&1== 1 else print(\"even\")\n",
        "#wap to fine the largest of two number\n"
      ],
      "metadata": {
        "id": "jrtt2kFHWohO",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "49e8b72b-4e9a-4c68-e631-4496de6d3582"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter num:2\n",
            "even\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "num1 = int(input(\"enter num1:\"))\n",
        "num2 =int(input(\"enter num2\"))\n",
        "print(\"num1 is greater than num2\") if num1 > num2 else print(\"num2 is graeter than num2\") "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "g_1S1TjDezEM",
        "outputId": "fe6ec563-b97f-4e3d-c2ba-3ac00d22662a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter num1:1\n",
            "enter num22\n",
            "num2 is graeter than num2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "num1 = int(input(\"enter num1:\"))\n",
        "num2 =int(input(\"enter num2:\"))\n",
        "num3 = int(input(\"enter num3:\"))\n",
        "a = 0\n",
        "print(\"num1\") if num1 > num2 or num1 > num3 else print(\"num3\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "20Q1Z6lDjJB7",
        "outputId": "ac50bd4f-9812-4b3c-d51e-07e9ddbeaa7e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter num1:10\n",
            "enter num2:3\n",
            "enter num3:5\n",
            "num1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "num1 = int(input(\"enter num1:\"))\n",
        "num2 =int(input(\"enter num2:\"))\n",
        "num3 = int(input(\"enter num3:\"))\n",
        "a = num1 if num1 > num2 else num2\n",
        "a = a if a > num3 else num3\n",
        "print(a) "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Bsk8u3KikXLT",
        "outputId": "bc3662d4-10b9-460f-fed3-f665d956df85"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter num1:1\n",
            "enter num2:4\n",
            "enter num3:2\n",
            "4\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#wap to create list of 3 friend.check if amit is present in the list or not if amit is not in the list append/add amit in the list\n",
        "friend = [\"rohit\",\"riya\",\"aditya\",\"nishant\",\"aryan\"]\n",
        "print(\"add amit\",friend.append('amit')) if \"amit\" not in friend else print('list',friend)\n",
        "print(friend)  "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "y77e9xCOncUL",
        "outputId": "766dc290-731c-4299-f9af-64cc264046bd"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "add amit None\n",
            "['rohit', 'riya', 'aditya', 'nishant', 'aryan', 'amit']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a = \"rohit mandal\"\n",
        "print(a.title())\n",
        "print(id(a))\n",
        "a = [\"r\",\"o\",\"s\",\"i\"]\n",
        "print(len(a))"
      ],
      "metadata": {
        "id": "A-PXWTNYo2fK",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "6a9c3e2c-9e07-433c-93ae-0a920a18b8e5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Rohit Mandal\n",
            "140399806527408\n",
            "4\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a = (1,\"hey\",3.4)\n",
        "print(a)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RfVn_XQPr_L5",
        "outputId": "1c82dadd-7c37-4eba-f760-47085e18ab41"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "(1, 'hey', 3.4)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"rohit \\n riya\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "419D3fwAtu3k",
        "outputId": "3cd147ac-0708-481d-c2ac-b47ce98a49d7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "rohit \n",
            " riya\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "num=input(\"enter num(only 3 dig):\")\n",
        "total = int(num[0])+int(num[1])+int(num[2])\n",
        "print(total)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cnJmynn7vgJE",
        "outputId": "573e4fbe-a4a1-4b80-d254-910d355f0e10"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter num(only 3 dig):222\n",
            "6\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "name =\"rohit\"\n",
        "print(name[5:0:-1])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qwkSyJhmwM-v",
        "outputId": "8c564984-49d8-45c1-e55b-667f7a7e42f2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "tiho\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "num = int(input(\"enter:\"))\n",
        "print(\"even\") if num%2 == 0 else  print(\"odd\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wg7QeUOtyI__",
        "outputId": "8c7e2e2f-50d6-4239-fd1b-28e5c202184e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter:4\n",
            "even\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#python class 9\n",
        "print(\"5 != 4:\",5 != 4)\n",
        "print(\"6 == 6:\",6 == 6)\n",
        "print(\"8 <= 10:\",8 <= 10)\n",
        "print(\"10 >= 9:\",10 >= 9)\n",
        "print(\"19 >=100:\",19 >=100)\n",
        "a = 11\n",
        "b = 2\n",
        "c = 10\n",
        "print((a>b) and (a > c))\n",
        "print((a<c)and (c<b))\n",
        "print((a<c) or (c<b))\n",
        "v=((a<c) or (c<b))\n",
        "print(not v )\n",
        "v =((a<c)and (c<b))\n",
        "print(not v)\n",
        "print(1 << 6)\n",
        "a += 10\n",
        "print(a)\n",
        "a-=10\n",
        "print(a)\n",
        "a **= 12\n",
        "print(a)\n",
        "a /= 6\n",
        "print(a)\n",
        "print(a is b)\n",
        "print(a is c)\n",
        "print(a is not b)\n",
        "print(a is not c)\n",
        "a = [\"amit\",\"riya\",\"rohit\"]\n",
        "b = 'rohit'\n",
        "print(b in a)"
      ],
      "metadata": {
        "id": "PKifH1dX1CWb",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "06cfd701-5b8b-44ab-9421-ae2fb974e9c3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5 != 4: True\n",
            "6 == 6: True\n",
            "8 <= 10: True\n",
            "10 >= 9: True\n",
            "19 >=100: False\n",
            "True\n",
            "False\n",
            "False\n",
            "True\n",
            "True\n",
            "64\n",
            "21\n",
            "11\n",
            "3138428376721\n",
            "523071396120.1667\n",
            "False\n",
            "False\n",
            "True\n",
            "True\n",
            "True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import random as rd\n",
        "a = [1,2,3,4,5]\n",
        "num = (rd.randint(1,3))\n",
        "print(rd.choice(a))\n",
        "if num == 1:\n",
        "  print(\"only 1 player can play\")\n",
        "elif num == 2:\n",
        "  print(\"only 2 player can play\")\n",
        "else :\n",
        "  print(\"only 3 player can play\")    \n",
        "for i in range(1,10):#n-1\n",
        "  print('rohit')  \n",
        "  print(i)\n",
        "while True:\n",
        "  print(\"rohit mandal\")\n",
        "  num = rd.randint(1,2)\n",
        "  if num == 2\n",
        "    "
      ],
      "metadata": {
        "id": "Jf-87K4HjERb",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "8f6c25c9-efbe-40a5-a380-55e4aca5917a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2\n",
            "only 1 player can play\n",
            "rohit\n",
            "1\n",
            "rohit\n",
            "2\n",
            "rohit\n",
            "3\n",
            "rohit\n",
            "4\n",
            "rohit\n",
            "5\n",
            "rohit\n",
            "6\n",
            "rohit\n",
            "7\n",
            "rohit\n",
            "8\n",
            "rohit\n",
            "9\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"sit nagpur \\n\"*100)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "i8VDKXHtUJeo",
        "outputId": "7d8ffea7-e9c3-42da-b742-97ead27ee50b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "sit nagpur \n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a = int(input(\"enter a number1:\"))\n",
        "b = int(input(\"enter a number2:\"))\n",
        "c = int(input(\"enter a number3:\"))\n",
        "if a > b:\n",
        "  print(a,\"is greatest then\",b)\n",
        "if a > c:\n",
        "  print(a,\"is greatest then\",c)\n",
        "if b > a :\n",
        "  print(b,\"is greatest then\",a)\n",
        "if b > c:\n",
        "  print(b ,\"is greatest then\",c)\n",
        "if c > a:\n",
        "  print(c,\"is greatest then\",a)\n",
        "if c > b:\n",
        "  print(c,\"is greatest then\",b) \n",
        "          "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4FkBKMgKXWuG",
        "outputId": "5f51fa76-e3d1-4108-dc44-f0d04e4c0463"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter a number1:1\n",
            "enter a number2:107239\n",
            "enter a number3:2073164646196\n",
            "107239 is greatest then 1\n",
            "2073164646196 is greatest then 1\n",
            "2073164646196 is greatest then 107239\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import random\n",
        "list1=[\"rock\",\"paper\",\"scissor\"]\n",
        "user = str(input(\"enter your choice [rock,paper,scissor]\"))\n",
        "computer = list1[random.randint(0,3)]\n",
        "print(\"computer choice\",computer)\n",
        "if user  == computer:\n",
        "  print(\"tie\")\n",
        "elif user == \"rock\":\n",
        "     if computer == \"paper\":\n",
        "       print(\"you win\")\n",
        "     else:\n",
        "       print(\"you loose\")\n",
        "elif user == \"paper\":\n",
        "     if computer == \"scissor\":\n",
        "       print(\"you loose\")\n",
        "     else:\n",
        "       print(\"you win\")\n",
        "elif user == \"scissor\":\n",
        "     if computer ==\"paper\":\n",
        "       print(\"you win\")\n",
        "     else :\n",
        "       print(\"you loose\")\n",
        "else:\n",
        "    print(\"error\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0Onvrnc2cqVw",
        "outputId": "d447b909-719f-4222-929b-9da5a8898ae9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter your choice [rock,paper,scissor]rock\n",
            "computer choice paper\n",
            "you win\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import random\n",
        "list1=[\"rock\",\"paper\",\"scissor\"]\n",
        "user = str(input(\"enter your choice [rock,paper,scissor]\"))\n",
        "computer = list1[random.randint(0,3)]\n",
        "print(\"computer choice\",computer)\n",
        "if user  == computer:\n",
        "  print(\"tie\")\n",
        "if user == \"rock\":\n",
        "     if computer == \"scissor\":\n",
        "       print(\"you win\")\n",
        "     if computer == \"paper\":\n",
        "       print(\"you loose\")\n",
        "if user == \"paper\":\n",
        "     if computer == \"scissor\":\n",
        "       print(\"you loose\")\n",
        "     if computer == \"rock\":\n",
        "       print(\"you win\")\n",
        "if user == \"scissor\":\n",
        "     if computer ==\"paper\":\n",
        "       print(\"you win\")\n",
        "     if computer == \"rock\" :\n",
        "       print(\"you loose\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "W2cwpUCgkLMJ",
        "outputId": "fc5b00b9-f170-43a9-827c-305eafc35256"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter your choice [rock,paper,scissor]paper\n",
            "computer choice paper\n",
            "tie\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "num = float(input(\"enter you num:\"))\n",
        "if num%2 == 0:\n",
        "  print(\"even\")\n",
        "if num%2 == 1:\n",
        "  print(\"odd\")  \n",
        "num = float(input(\"enter you num:\"))\n",
        "if num > 0:\n",
        "  print('postive')\n",
        "if num < 0:\n",
        "  print('negative') \n",
        "if num == 0:\n",
        "  print(num)     "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "T1R--Bb5nbU5",
        "outputId": "f4e68529-e224-4e0c-f7fb-9509a5fc55bb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter you num:-271937\n",
            "odd\n",
            "enter you num:-7391278\n",
            "negative\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#wap to get two number form input from user perform addition if the sec num is multiple of first other wise perform substracion\n",
        "num1 = int(input(\"enter your number1:\"))\n",
        "num2 = int(input(\"enter your number2:\"))\n",
        "\n",
        "if num1%num2 == 0:\n",
        "  print(num1+num2)\n",
        "if num2%num1 != 0:\n",
        "  print(num1*num2)  "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-nCW_n6oobNG",
        "outputId": "c579abe3-1b9e-4b8c-ae04-b30e286f6f2d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter your number1:123\n",
            "enter your number2:12\n",
            "1476\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "animal_list = [\"cat\",\"rat\",\"tiger\",\"python\"]\n",
        "if \"lion\" in animal_list:\n",
        "  print(\"already there sir\")\n",
        "else:\n",
        "  animal_list.append(\"lion\")\n",
        "  print(\"done sir\")\n",
        "\n",
        "print(animal_list)    "
      ],
      "metadata": {
        "id": "ih7pCh_eqoot",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "d7288f55-26a3-41e2-b2f2-c8744f57e3d9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "done sir\n",
            "['cat', 'rat', 'tiger', 'python', 'lion']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#wap to find wether a number is even or odd using if else\n",
        "num = float(input(\"enter number:\"))\n",
        "if num%2 == 0:\n",
        "  print(\"even\")\n",
        "else:\n",
        "  print('odd')  "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hjXXFXVokxXb",
        "outputId": "544e248e-a5be-497b-d06f-1e04187f73d2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter number:122\n",
            "even\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#wap to check weather a num enter by user is greater then 30 or equal to 30 greater then 30\n",
        "num = int(input(\"enter a number:\"))\n",
        "if num <= 30:\n",
        "  if num == 30 :\n",
        "      print(\"num is equal to 30\")\n",
        "  else: \n",
        "      print(\"num is smaller then 30\")    \n",
        "else :\n",
        "  print(\"num is greater then 30\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OSaET5iPlX-V",
        "outputId": "4f5b43af-be47-4ae3-d814-1a17c95c4c01"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter a number:56\n",
            "num is greater then 30\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "num = int(input(\"enter your num:\"))\n",
        "if num < 30:\n",
        "    print(\"num is smaller then 30\")  \n",
        "elif num == 30 :\n",
        "    print(\"num is equal to 30\")  \n",
        "else :\n",
        "    print(\"num is greater then 30\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XrPGBhOcmBCu",
        "outputId": "a4ceebab-2ff7-40e6-abf0-1877d21545f4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter your num:56\n",
            "num is greater then 30\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#wap to print grade of students base on the percentage sports if 90 up A+ if 80-90 A 70-80 b+ 70-60 b 60-50 c+ 40-50 c less then 40 fail\n",
        "name = str(input(\"enter your name:\"))\n",
        "num = int(input(\"enter your marks:\"))\n",
        "if num > 90 and num <= 100 :\n",
        "    print(f\"cong {name} you got A+\")\n",
        "elif num >= 80 and num <= 90 :\n",
        "    print(f\"cong {name} you got A\")\n",
        "elif num >= 70 and num <= 79 :\n",
        "    print(f\"cong {name} you got B+\")      \n",
        "elif num >= 60 and num <= 69:\n",
        "    print(f\"cong {name} you got B\")\n",
        "elif num >= 50 and num <= 59:\n",
        "    print(f\"cong {name} you got c+\")\n",
        "elif num >= 40 and num <= 49:\n",
        "    print(f\"cong {name} you got c\") \n",
        "elif num < 40 :\n",
        "    print(f\"sorry {name} you have failed\")\n",
        "else:\n",
        "    print(\"invalid input\")                                        "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "J6XMMpnxrGjG",
        "outputId": "bc93387d-481c-4b26-9f0d-3c853b5acf87"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter your name:rohit\n",
            "enter your marks:100\n",
            "cong rohit you got A+\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(10):\n",
        "   print(i)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "obA4zp81wAzz",
        "outputId": "f8a82f25-7584-41fd-a3fc-ddc18ba0b7ab"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0\n",
            "1\n",
            "2\n",
            "3\n",
            "4\n",
            "5\n",
            "6\n",
            "7\n",
            "8\n",
            "9\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "num = int(input(\"enter you number\"))\n",
        "for i in range(1,11):\n",
        "    print(f\"{num}*{i} =\",i*num)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uE9tD9vgxwkK",
        "outputId": "a3326f02-96c1-4230-a218-9e2b03b0bbb3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter you number6\n",
            "6*1 = 6\n",
            "6*2 = 12\n",
            "6*3 = 18\n",
            "6*4 = 24\n",
            "6*5 = 30\n",
            "6*6 = 36\n",
            "6*7 = 42\n",
            "6*8 = 48\n",
            "6*9 = 54\n",
            "6*10 = 60\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(1,101):\n",
        "  print(\"symbiosis institute of technology ,nagpur\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Q6r_ZEKmylwS",
        "outputId": "603c1c6b-b20a-4f74-a77d-68667fbea0f7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n",
            "symbiosis institute of technology ,nagpur\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "friend =[\"aditya\",\"nishant\",\"aryan\",\"prathm\",\"rohit\"]\n",
        "for i in friend:\n",
        "     print(i,\"number of character\",len(i))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EkY0kx5Azf36",
        "outputId": "fd2fde16-2607-413f-9822-58cbb86d562c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "aditya number of character 6\n",
            "nishant number of character 7\n",
            "aryan number of character 5\n",
            "prathm number of character 6\n",
            "rohit number of character 5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "bear = {\"grizzly\":\"angry\",\"brown\":\"friendly\",\"polar\":\"friendly\"}\n",
        "for bears in bear:\n",
        "    if bear[bears] == \"friendly\":\n",
        "      print(\"hello \",bears,\"bear\")\n",
        "    else:\n",
        "      print(\"bad bear\")  "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SULbQ7YQ1jHj",
        "outputId": "429ab5a6-eddf-48a3-f57c-4041b96f2d3d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "bad bear\n",
            "hello  brown bear\n",
            "hello  polar bear\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#wap to print all prime num within a give range\n",
        "num1 = int(input(\"enter your stop timeing:\"))\n",
        "num2 = int(input(\"enter your stop timeing:\"))\n",
        "a = 1\n",
        "for i in range(num1,num2+1):\n",
        "    if i == 2:\n",
        "        print (\"2 is prime number\")\n",
        "    elif i == 1:\n",
        "        print (\"1 is prime number\")\n",
        "    elif i == 3:\n",
        "        print (\"3 is prime number\")\n",
        "    elif i == 5:\n",
        "        print(\"5 is prime number\")\n",
        "    elif i == 7:\n",
        "        print(\"7 is prime number\")            \n",
        "    else:\n",
        "        if i%2 == 0:\n",
        "            a += 1\n",
        "        elif i%3 == 0:\n",
        "            a += 1\n",
        "        elif i%5 == 0:\n",
        "            a += 1    \n",
        "        elif i%7 == 0:\n",
        "            a += 1     \n",
        "        else:\n",
        "            print (i,\"is prime number\")\n",
        "print (\"none prime number =\",a)\n"
      ],
      "metadata": {
        "id": "SaMV-Syf69x0",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "87089c90-1f08-425a-9f4e-b0d3479c6d3c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter your stop timeing:31\n",
            "enter your stop timeing:41\n",
            "31 is prime number\n",
            "37 is prime number\n",
            "41 is prime number\n",
            "none prime number = 9\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a = int(input(\"start:\"))\n",
        "b =int(input(\"stop:\"))\n",
        "for i in range(a,b+1):\n",
        "  for j in range(2,i):\n",
        "    if i%j==0:\n",
        "      break\n",
        "  else:\n",
        "    print(i)  "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3W9af0cmZ29a",
        "outputId": "724eef86-0872-46a2-b1bd-b52d83b310fa"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "start:1\n",
            "stop:20\n",
            "1\n",
            "2\n",
            "3\n",
            "5\n",
            "7\n",
            "11\n",
            "13\n",
            "17\n",
            "19\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#odd even number\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OWQsRfYziZKu",
        "outputId": "c89825c4-22ee-4697-99fa-daaab2cf8e31"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "99999999999999999999999999999999999999999999999999999999999999999999969999999999999999999999999999999999999999999999999999996999999999999999999999999999999999999999969999999999999999999999999999999999999996\n",
            "even number\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "n =1\n",
        "for i in range(5):\n",
        "  print(\"* \"*n)\n",
        "  n +=1"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Xst4M4Jfl0Vn",
        "outputId": "b4634c43-21cb-4ed0-e4fa-8fd03a536cb1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "* \n",
            "* * \n",
            "* * * \n",
            "* * * * \n",
            "* * * * * \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "n = int(input(\"user input\"))\n",
        "for i in range(n,0,-1):\n",
        "  print(\"* \"*n)\n",
        "  n-=1\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fjEYxIK0ndkb",
        "outputId": "5ed1cf56-c5d0-414c-9df2-4d2769a9b233"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "user input5\n",
            "* * * * * \n",
            "* * * * \n",
            "* * * \n",
            "* * \n",
            "* \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "n = 1\n",
        "m = 0\n",
        "apl=[\"A\",\"B\",\"C\",\"D\"]\n",
        "for i in range(4,0,-1):\n",
        "  print(f\"{apl[m]} \"*n)\n",
        "  m += 1\n",
        "  n += 1"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yTMX9Bq9pPKo",
        "outputId": "3eaaa66a-cc32-4507-867d-0a5b91275d27"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "A \n",
            "B B \n",
            "C C C \n",
            "D D D D \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "n = int(input(\"Enter the number of rows: \"))  \n",
        "m = (2 * n) - 2  \n",
        "for i in range(0, n):  \n",
        "    for j in range(0, m):  \n",
        "        print(end=\" \")  \n",
        "    m = m - 1   \n",
        "    for j in range(0, i + 1):   \n",
        "        print( \"* \", end=' ')  \n",
        "    print(\" \")  "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NkTiYyfqqyV7",
        "outputId": "fccafe05-e2e8-4b96-89fa-f06162574884"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the number of rows: 5\n",
            "        *   \n",
            "       *  *   \n",
            "      *  *  *   \n",
            "     *  *  *  *   \n",
            "    *  *  *  *  *   \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "n = int(input(\"Enter the number of rows: \"))  \n",
        "apl =[\"a\",\"b\",\"c\",\"d\"]\n",
        "m = (2 * n) - 2  \n",
        "for i in range(0, n):  \n",
        "    for j in range(0, m):  \n",
        "        print(end=\" \")  \n",
        "    m = m - 1   \n",
        "    for j in range(0, i + 1):   \n",
        "        print(\"*\", end=' ')  \n",
        "    print(\" \")  "
      ],
      "metadata": {
        "id": "Qj7c5LYJuALX",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "f1ee8c8f-475d-47f7-d916-47188c8594e8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the number of rows: 5\n",
            "        *  \n",
            "       * *  \n",
            "      * * *  \n",
            "     * * * *  \n",
            "    * * * * *  \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#while luop\n",
        "#wap to find sum of digits of a number given by user\n",
        "num = int(input())\n",
        "sum =0\n",
        "while (num > 0):\n",
        "    digit = num % 10\n",
        "    sum += digit\n",
        "    num = num//10 \n",
        "print(sum) "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LzJDzDYOkFwM",
        "outputId": "7fab193e-1cd4-49ba-b71b-e371c2e461b6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "44\n",
            "8\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "num = str(input())\n",
        "sum =0\n",
        "for i in num:\n",
        "  sum += int(i)\n",
        "print(sum)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mLFHpJRGoPIb",
        "outputId": "deeb66d5-e54c-4a1b-e134-eb51a72893af"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "145\n",
            "10\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "n = int(input())\n",
        "numB,z =n,0\n",
        "count =0\n",
        "while (n != 0):\n",
        "  count +=1\n",
        "  n = n//10\n",
        "  z += 1\n",
        "sum1,k= 0,numB\n",
        "while (numB != 0):\n",
        "  sum1 += pow(numB%10,count)\n",
        "  numB = numB//10\n",
        "if sum1==k:\n",
        "  print(\"arm\")\n",
        "else:\n",
        "  print(\"not arm\")  \n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Gdjmwla0qXX_",
        "outputId": "9c91098b-9c45-496e-87b5-a037bda9e82e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "125\n",
            "not arm\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "p = int(input())\n",
        "z = 0\n",
        "while (p > 0):\n",
        "    p = p//10\n",
        "    z +=1 # z +=1\n",
        "print(z)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BWMEb-6MsAt-",
        "outputId": "d588d977-e3e9-42f7-d4cd-4ad4c7d05662"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "4545\n",
            "4\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(1,100):\n",
        "  print(\"hello wrold\")\n",
        "  if i == 20:\n",
        "    pass\n",
        "  elif i ==50:\n",
        "    print(\"go\")\n",
        "    continue\n",
        "    print(\"do not go\")\n",
        "  elif i == 99:\n",
        "    break\n",
        "  else:\n",
        "    print(i)    \n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Lqwy2KRhvGH5",
        "outputId": "38269ed4-a6b2-4dd0-a24b-1c55453c591b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "hello wrold\n",
            "1\n",
            "hello wrold\n",
            "2\n",
            "hello wrold\n",
            "3\n",
            "hello wrold\n",
            "4\n",
            "hello wrold\n",
            "5\n",
            "hello wrold\n",
            "6\n",
            "hello wrold\n",
            "7\n",
            "hello wrold\n",
            "8\n",
            "hello wrold\n",
            "9\n",
            "hello wrold\n",
            "10\n",
            "hello wrold\n",
            "11\n",
            "hello wrold\n",
            "12\n",
            "hello wrold\n",
            "13\n",
            "hello wrold\n",
            "14\n",
            "hello wrold\n",
            "15\n",
            "hello wrold\n",
            "16\n",
            "hello wrold\n",
            "17\n",
            "hello wrold\n",
            "18\n",
            "hello wrold\n",
            "19\n",
            "hello wrold\n",
            "hello wrold\n",
            "21\n",
            "hello wrold\n",
            "22\n",
            "hello wrold\n",
            "23\n",
            "hello wrold\n",
            "24\n",
            "hello wrold\n",
            "25\n",
            "hello wrold\n",
            "26\n",
            "hello wrold\n",
            "27\n",
            "hello wrold\n",
            "28\n",
            "hello wrold\n",
            "29\n",
            "hello wrold\n",
            "30\n",
            "hello wrold\n",
            "31\n",
            "hello wrold\n",
            "32\n",
            "hello wrold\n",
            "33\n",
            "hello wrold\n",
            "34\n",
            "hello wrold\n",
            "35\n",
            "hello wrold\n",
            "36\n",
            "hello wrold\n",
            "37\n",
            "hello wrold\n",
            "38\n",
            "hello wrold\n",
            "39\n",
            "hello wrold\n",
            "40\n",
            "hello wrold\n",
            "41\n",
            "hello wrold\n",
            "42\n",
            "hello wrold\n",
            "43\n",
            "hello wrold\n",
            "44\n",
            "hello wrold\n",
            "45\n",
            "hello wrold\n",
            "46\n",
            "hello wrold\n",
            "47\n",
            "hello wrold\n",
            "48\n",
            "hello wrold\n",
            "49\n",
            "hello wrold\n",
            "go\n",
            "hello wrold\n",
            "51\n",
            "hello wrold\n",
            "52\n",
            "hello wrold\n",
            "53\n",
            "hello wrold\n",
            "54\n",
            "hello wrold\n",
            "55\n",
            "hello wrold\n",
            "56\n",
            "hello wrold\n",
            "57\n",
            "hello wrold\n",
            "58\n",
            "hello wrold\n",
            "59\n",
            "hello wrold\n",
            "60\n",
            "hello wrold\n",
            "61\n",
            "hello wrold\n",
            "62\n",
            "hello wrold\n",
            "63\n",
            "hello wrold\n",
            "64\n",
            "hello wrold\n",
            "65\n",
            "hello wrold\n",
            "66\n",
            "hello wrold\n",
            "67\n",
            "hello wrold\n",
            "68\n",
            "hello wrold\n",
            "69\n",
            "hello wrold\n",
            "70\n",
            "hello wrold\n",
            "71\n",
            "hello wrold\n",
            "72\n",
            "hello wrold\n",
            "73\n",
            "hello wrold\n",
            "74\n",
            "hello wrold\n",
            "75\n",
            "hello wrold\n",
            "76\n",
            "hello wrold\n",
            "77\n",
            "hello wrold\n",
            "78\n",
            "hello wrold\n",
            "79\n",
            "hello wrold\n",
            "80\n",
            "hello wrold\n",
            "81\n",
            "hello wrold\n",
            "82\n",
            "hello wrold\n",
            "83\n",
            "hello wrold\n",
            "84\n",
            "hello wrold\n",
            "85\n",
            "hello wrold\n",
            "86\n",
            "hello wrold\n",
            "87\n",
            "hello wrold\n",
            "88\n",
            "hello wrold\n",
            "89\n",
            "hello wrold\n",
            "90\n",
            "hello wrold\n",
            "91\n",
            "hello wrold\n",
            "92\n",
            "hello wrold\n",
            "93\n",
            "hello wrold\n",
            "94\n",
            "hello wrold\n",
            "95\n",
            "hello wrold\n",
            "96\n",
            "hello wrold\n",
            "97\n",
            "hello wrold\n",
            "98\n",
            "hello wrold\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#home work\n",
        "ranges = int(input())\n",
        "for i in range(ranges):\n",
        "    n = int(input())\n",
        "    numB,z =n,0\n",
        "    count =0\n",
        "    while (n != 0):\n",
        "      count +=1\n",
        "      n = n//10\n",
        "      z += 1\n",
        "    sum1,k= 0,numB\n",
        "    while (numB != 0):\n",
        "      sum1 += pow(numB%10,count)\n",
        "      numB = numB//10\n",
        "    if sum1==k:\n",
        "      print(\"arm\")\n",
        "    else:\n",
        "      print(\"not arm\")  \n",
        "      "
      ],
      "metadata": {
        "id": "P0xFfdU0-eYP",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "874e3c7a-a12c-4697-ab97-f8fba3a29a28"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2\n",
            "317\n",
            "not arm\n",
            "153\n",
            "arm\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "num_start = int(input())\n",
        "num_stop =int(input())\n",
        "sum = num_start\n",
        "n1,n2 =num_start,num_start+1\n",
        "print(\"==============x===========\")\n",
        "for i in range(num_start,num_stop):\n",
        "    print(sum )\n",
        "    n1=n2\n",
        "    n2=sum\n",
        "    sum = n1+n2\n",
        "    "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eJMyL1NdXY_T",
        "outputId": "64988463-f766-422e-efe3-3ee4aa1d8f79"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "45\n",
            "50\n",
            "==============x===========\n",
            "45\n",
            "91\n",
            "136\n",
            "227\n",
            "363\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def add(x,y):\n",
        "  '''add function'''\n",
        "  return x + y\n",
        "\n",
        "def power(x):\n",
        "  #power function\n",
        "  return x**2 , x**3\n",
        "\n",
        "def aryan():\n",
        "   for i in range(1,10):\n",
        "     print()   \n",
        "def sumofdigit(num):\n",
        "  sum =0\n",
        "  while (num!=0):\n",
        "    sum = sum + num%10\n",
        "    num = num//10\n",
        "  print(sum)  \n",
        "if __name__==\"__main__\":\n",
        "  num = int(input(\"enter num:\"))\n",
        "  sumofdigit(num) "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wE16Rfc1qnbD",
        "outputId": "4e12a46d-7c5d-4135-e4a5-7133fa4bddc1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter num:4464464\n",
            "32\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def grade(name,num):\n",
        "  if num > 90 and num <= 100 :\n",
        "     print(f\"cong {name} you got A+\")\n",
        "  elif num >= 80 and num <= 90 :\n",
        "      print(f\"cong {name} you got A\")\n",
        "  elif num >= 70 and num <= 79 :\n",
        "     print(f\"cong {name} you got B+\")      \n",
        "  elif num >= 60 and num <= 69:\n",
        "      print(f\"cong {name} you got B\")\n",
        "  elif num >= 50 and num <= 59:\n",
        "      print(f\"cong {name} you got c+\")\n",
        "  elif num >= 40 and num <= 49:\n",
        "      print(f\"cong {name} you got c\") \n",
        "  elif num < 40 :\n",
        "      print(f\"sorry {name} you have failed\")\n",
        "  else:\n",
        "     print(\"invalid input\")    \n",
        "if __name__==\"__main__\":\n",
        "  num = int(input(\"enter your marks:\"))\n",
        "  name = str(input(\"enter your name:\"))\n",
        "  grade(name,num)                                         "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Zcnrl-XrsMEK",
        "outputId": "a94eb568-f75d-486a-b452-23aaf51d7b0c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter your marks:40\n",
            "enter your name:aryan\n",
            "cong aryan you got c\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "help(add)\n",
        "add.__doc__"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jdemukqBvGT4",
        "outputId": "3ad50bb1-d433-42b3-8622-c3d0a8c3fc2a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Help on function add in module __main__:\n",
            "\n",
            "add(x, y)\n",
            "    add function\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def fibb(stop):\n",
        "   num_start = 0\n",
        "   num_stop = stop\n",
        "   sum = num_start\n",
        "   n1,n2 =num_start,num_start+1\n",
        "   for i in range(num_start,num_stop):\n",
        "       print(sum )\n",
        "       n1=n2\n",
        "       n2=sum\n",
        "       sum = n1+n2\n",
        "\n",
        "if __name__==\"__main__\":\n",
        "    stop = int(input(\"enter range:\"))\n",
        "    fibb(stop)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MfVzuos_w4Ku",
        "outputId": "acd8e8fe-f543-45e4-d397-d0f6d7601679"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter range:10\n",
            "0\n",
            "1\n",
            "1\n",
            "2\n",
            "3\n",
            "5\n",
            "8\n",
            "13\n",
            "21\n",
            "34\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def fibb(stop):\n",
        "   num= stop\n",
        "   sum = 0\n",
        "   n1,n2 =0,1\n",
        "   while num > sum: \n",
        "       print(sum )\n",
        "       n1=n2\n",
        "       n2=sum\n",
        "       sum = n1+n2\n",
        "\n",
        "if __name__==\"__main__\":\n",
        "    stop = int(input(\"enter range:\"))\n",
        "    fibb(stop)      "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BfOW-MLDzjlE",
        "outputId": "23085d5f-33c4-47a5-fc87-188f47db6aee"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter range:45\n",
            "0\n",
            "1\n",
            "1\n",
            "2\n",
            "3\n",
            "5\n",
            "8\n",
            "13\n",
            "21\n",
            "34\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def fibbo(n):\n",
        "  a,b =0,1\n",
        "  while a < n:\n",
        "    print(a,end=\" \")\n",
        "    a,b =b,a+b\n",
        "fibbo(10)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "K7aeFvZO1wME",
        "outputId": "dbacfb8f-088a-489b-da9e-76f478d444ab"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0 1 1 2 3 5 8 "
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def f():\n",
        "  y = 5\n",
        "  print(f'inside function y is :{y} & id :{id(y)} ')\n",
        "  x = 5\n",
        "  print(f'inside function y is :{x} & id :{id(x)} ')\n",
        "f()  \n",
        "y"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "o92bbnro7C0r",
        "outputId": "a14b36a6-26a8-4bd6-a013-bf880ad6f8e7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "inside function y is :5 & id :11126816 \n",
            "inside function y is :5 & id :11126816 \n",
            "inside function y is :10 & id :11126976 \n",
            "inside function y is :5 & id :11126816 \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def f(x):\n",
        "  x = [\"nagpur\",\"pune\",\"mumbai\",\"nasik\"]\n",
        "city_list = [\"nagpur\",\"pune\",\"mumbai\",\"nasik\"]\n",
        "print(f\"pro outside function city_list is:{city_list} and is:{id(city_list)}\")\n",
        "f(city_list)\n",
        "print(f\"outside function city_list is :{city_list} and id:{id(city_list)}\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5P_Ctu5996cY",
        "outputId": "2fcf7eb8-d402-4ff6-e462-2af59b8e1227"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "pro outside function city_list is:['nagpur', 'pune', 'mumbai', 'nasik'] and is:139735626963456\n",
            "outside function city_list is :['nagpur', 'pune', 'mumbai', 'nasik'] and id:139735626963456\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# wap to reverse \n",
        "def rev(n):\n",
        "  x =0\n",
        "  while n!=0:\n",
        "    x =x*10+n%10\n",
        "    n = n//10\n",
        "  print(x) \n",
        "\n",
        "#wap to create a function that insert an element of list at aparticular position\n",
        "x = []\n",
        "def  ins():\n",
        "   x.insert(0,1)\n",
        "   x.insert(5,5)\n",
        "   x.insert(2,3)\n",
        "   print(x) \n",
        "x = [29,36,63,255,990]\n",
        "print(x)\n",
        "print(\"update\")\n",
        "u = [1,2,3,34,57,45,646,8293]\n",
        "def new():\n",
        "    print(u)\n",
        "    user = \"y\"\n",
        "    while user != \"n\":\n",
        "      a= int(input(\"enter position:\"))\n",
        "      b=int(input(\"enter element:\"))\n",
        "      u.insert(a-1,b) \n",
        "      user = str(input(\"do you want to continue(y,n):\"))\n",
        "    print(u)\n",
        "      \n",
        " #if we use default argument it will follow by non defult argument\n",
        "def p(x=1,y=1,z=1):\n",
        "    return ( x ** y **z)\n",
        "print(p(1))\n",
        "print(p(11,3))\n",
        "print(p(2,2,3))\n",
        "\n",
        "i=5\n",
        "print(f'The argument outside before function is {i}')\n",
        "def f(arg=i):\n",
        "  print(f'The argument is {arg} & {id(arg)}')\n",
        "\n",
        "  i=6\n",
        "  f(6)\n",
        "  f()\n",
        "  print(f'The argument outside after function is {i} & {id(i)}')\n",
        "def f(a = 1,l=[]):\n",
        "  l.append(a)\n",
        "  print(id(l),end=\":\")\n",
        "  print( l, end=\"\\n\" ) \n",
        "f()\n",
        "f(2)\n",
        "f(3)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-mNVKSDscpHX",
        "outputId": "bde45f61-a1a1-4b58-bc2d-9a018f3e6335"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[29, 36, 63, 255, 990]\n",
            "update\n",
            "1\n",
            "1331\n",
            "256\n",
            "The argument outside before function is 5\n",
            "139735627402496:[1]\n",
            "139735627402496:[1, 2]\n",
            "139735627402496:[1, 2, 3]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Write a program using functions. Find function x & do not take any parameter as inout but creates a list of 5 friends. The function checks if the friend is present in the list or not.\n",
        "#It does nothing otherwise append the friend name in the list. \n",
        "def x():\n",
        "  l = [\"rohit\",\"nishant\",\"aditya\",\"aryan\",\"shreya\"]\n",
        "  for i in l:\n",
        "    if i == \"riya\":\n",
        "      continue\n",
        "    else:\n",
        "      break\n",
        "  l.append(\"riya\")      \n",
        "  print(l)\n",
        "x()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Mpb5xVT7zShE",
        "outputId": "ea5b27f1-483a-4932-8d02-426fa66d2dfe"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['rohit', 'nishant', 'aditya', 'aryan', 'shreya', 'riya']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "punctuations = '''!()-[]{};:'\"\\,<>./?@#$%^&*_~'''\n",
        "no_punct = \"\"\n",
        "my_str = str(input(\"enter string value:\"))\n",
        "for i in my_str:\n",
        "   if i not in punctuations:\n",
        "       no_punct = no_punct + i\n",
        "print(no_punct)"
      ],
      "metadata": {
        "id": "4n4agu1AN3uF",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "d37c54ec-c498-476d-9e23-0321da3c51e0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter string value:hello world : my self , rohit\n",
            "hello world  my self  rohit\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def student(name ,classs= \"12\",roll= \"23\"):\n",
        "    print(\"your name is \",name)\n",
        "    print(\"class :\",classs)\n",
        "    print(\"roll:\",roll)\n",
        "student(name = \"shreya rohit mandal \",roll = \"29\", classs=\"11\") \n"
      ],
      "metadata": {
        "id": "uqsueOi5QEO9",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "c05f998b-4c2b-4bb7-ac9e-2699af01aa09"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "your name is  shreya rohit mandal \n",
            "class : 11\n",
            "roll: 29\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#9/12/22\n",
        "x = lambda a:a+10\n",
        "print(x(5))\n",
        "y = lambda b:b+12\n",
        "print(y(7))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2NTT-0KHhAWA",
        "outputId": "a3782014-de0b-4bc2-940a-c54aaed743c9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "15\n",
            "19\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "list_number = [2,3,4,5,6,7]\n",
        "odd_count = list(filter(lambda x: (x%2 != 0) , list_number))\n",
        "even_count = list(filter(lambda x: (x%2 == 0) , list_number))\n",
        "print(\"Even numbers: \", even_count)\n",
        "print(\"Odd numbers : \", odd_count)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3Ew4hl_ulJ1U",
        "outputId": "6d35a3cb-ae5b-4acb-e1bb-467dca8a8c60"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Even numbers:  [2, 4, 6]\n",
            "Odd numbers :  [3, 5, 7]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "m  = (lambda x:\n",
        "      (x % 2 and \"odd\" or \"ever\"))(3)\n",
        "print(m)      "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gjxpp1DxvSrG",
        "outputId": "93f967ab-d627-465a-91f6-197f3bcab0ad"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "odd\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print((lambda x,y,z: x+y+z)(1,2,3))\n",
        "print((lambda x,y,z = 3:x+y+z)(1,2))\n",
        "print((lambda x,y,z=3:x+y+z)(1,y=2))\n",
        "print((lambda *args: sum(args))(1,2,3))\n",
        "print((lambda **kwargs: sum(kwargs.values()))(one=1,two=2,three=3))\n",
        "print((lambda x,*,y=0,z =0:x+y+z)(1,y=2,z=3))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2hujIxbtzsSI",
        "outputId": "2e0c0570-dee1-447a-b85d-b12cb16a829f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "6\n",
            "6\n",
            "6\n",
            "6\n",
            "6\n",
            "6\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#write a program to 5 number as a input at oncce to print factorial of each number using map function \n",
        "def fac():\n",
        "     a =  list(map(int,input().split()))\n",
        "     n = 0\n",
        "     product = 1\n",
        "     for j in a:\n",
        "         for i in range(a[n],0,-1):\n",
        "             product *=i \n",
        "         print(\"factorial of \",a[n],\"=\",product)    \n",
        "         n += 1\n",
        "fac()   \n",
        "      "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7CowzQAF4nc2",
        "outputId": "4e5f3b25-b908-4e8d-ff22-d83aad10183e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 2 3 4 5\n",
            "factorial of  1 = 1\n",
            "factorial of  2 = 2\n",
            "factorial of  3 = 12\n",
            "factorial of  4 = 288\n",
            "factorial of  5 = 34560\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import math\n",
        "def fac():\n",
        "  a = list(map(int,input().split()))\n",
        "  pst = list(map(math.factorial,a))\n",
        "  print(pst)\n",
        "if __name__==\"__main__\":\n",
        "  fac()  "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "h9UFPhlS7kHK",
        "outputId": "3d5e43e5-ab7f-44c3-94c3-b5130a1fdf47"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 2 3 4 5\n",
            "[1, 2, 6, 24, 120]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "dir(math)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "db-n5pMa-Nsb",
        "outputId": "5b49325b-ef0b-4a40-97bc-f3a8ff10295a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['__doc__',\n",
              " '__loader__',\n",
              " '__name__',\n",
              " '__package__',\n",
              " '__spec__',\n",
              " 'acos',\n",
              " 'acosh',\n",
              " 'asin',\n",
              " 'asinh',\n",
              " 'atan',\n",
              " 'atan2',\n",
              " 'atanh',\n",
              " 'ceil',\n",
              " 'comb',\n",
              " 'copysign',\n",
              " 'cos',\n",
              " 'cosh',\n",
              " 'degrees',\n",
              " 'dist',\n",
              " 'e',\n",
              " 'erf',\n",
              " 'erfc',\n",
              " 'exp',\n",
              " 'expm1',\n",
              " 'fabs',\n",
              " 'factorial',\n",
              " 'floor',\n",
              " 'fmod',\n",
              " 'frexp',\n",
              " 'fsum',\n",
              " 'gamma',\n",
              " 'gcd',\n",
              " 'hypot',\n",
              " 'inf',\n",
              " 'isclose',\n",
              " 'isfinite',\n",
              " 'isinf',\n",
              " 'isnan',\n",
              " 'isqrt',\n",
              " 'ldexp',\n",
              " 'lgamma',\n",
              " 'log',\n",
              " 'log10',\n",
              " 'log1p',\n",
              " 'log2',\n",
              " 'modf',\n",
              " 'nan',\n",
              " 'perm',\n",
              " 'pi',\n",
              " 'pow',\n",
              " 'prod',\n",
              " 'radians',\n",
              " 'remainder',\n",
              " 'sin',\n",
              " 'sinh',\n",
              " 'sqrt',\n",
              " 'tan',\n",
              " 'tanh',\n",
              " 'tau',\n",
              " 'trunc']"
            ]
          },
          "metadata": {},
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "help(math)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yny3foqnArIj",
        "outputId": "ca92ca54-31cf-42b0-a894-3046b97ca108"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Help on built-in module math:\n",
            "\n",
            "NAME\n",
            "    math\n",
            "\n",
            "DESCRIPTION\n",
            "    This module provides access to the mathematical functions\n",
            "    defined by the C standard.\n",
            "\n",
            "FUNCTIONS\n",
            "    acos(x, /)\n",
            "        Return the arc cosine (measured in radians) of x.\n",
            "    \n",
            "    acosh(x, /)\n",
            "        Return the inverse hyperbolic cosine of x.\n",
            "    \n",
            "    asin(x, /)\n",
            "        Return the arc sine (measured in radians) of x.\n",
            "    \n",
            "    asinh(x, /)\n",
            "        Return the inverse hyperbolic sine of x.\n",
            "    \n",
            "    atan(x, /)\n",
            "        Return the arc tangent (measured in radians) of x.\n",
            "    \n",
            "    atan2(y, x, /)\n",
            "        Return the arc tangent (measured in radians) of y/x.\n",
            "        \n",
            "        Unlike atan(y/x), the signs of both x and y are considered.\n",
            "    \n",
            "    atanh(x, /)\n",
            "        Return the inverse hyperbolic tangent of x.\n",
            "    \n",
            "    ceil(x, /)\n",
            "        Return the ceiling of x as an Integral.\n",
            "        \n",
            "        This is the smallest integer >= x.\n",
            "    \n",
            "    comb(n, k, /)\n",
            "        Number of ways to choose k items from n items without repetition and without order.\n",
            "        \n",
            "        Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates\n",
            "        to zero when k > n.\n",
            "        \n",
            "        Also called the binomial coefficient because it is equivalent\n",
            "        to the coefficient of k-th term in polynomial expansion of the\n",
            "        expression (1 + x)**n.\n",
            "        \n",
            "        Raises TypeError if either of the arguments are not integers.\n",
            "        Raises ValueError if either of the arguments are negative.\n",
            "    \n",
            "    copysign(x, y, /)\n",
            "        Return a float with the magnitude (absolute value) of x but the sign of y.\n",
            "        \n",
            "        On platforms that support signed zeros, copysign(1.0, -0.0)\n",
            "        returns -1.0.\n",
            "    \n",
            "    cos(x, /)\n",
            "        Return the cosine of x (measured in radians).\n",
            "    \n",
            "    cosh(x, /)\n",
            "        Return the hyperbolic cosine of x.\n",
            "    \n",
            "    degrees(x, /)\n",
            "        Convert angle x from radians to degrees.\n",
            "    \n",
            "    dist(p, q, /)\n",
            "        Return the Euclidean distance between two points p and q.\n",
            "        \n",
            "        The points should be specified as sequences (or iterables) of\n",
            "        coordinates.  Both inputs must have the same dimension.\n",
            "        \n",
            "        Roughly equivalent to:\n",
            "            sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))\n",
            "    \n",
            "    erf(x, /)\n",
            "        Error function at x.\n",
            "    \n",
            "    erfc(x, /)\n",
            "        Complementary error function at x.\n",
            "    \n",
            "    exp(x, /)\n",
            "        Return e raised to the power of x.\n",
            "    \n",
            "    expm1(x, /)\n",
            "        Return exp(x)-1.\n",
            "        \n",
            "        This function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x.\n",
            "    \n",
            "    fabs(x, /)\n",
            "        Return the absolute value of the float x.\n",
            "    \n",
            "    factorial(x, /)\n",
            "        Find x!.\n",
            "        \n",
            "        Raise a ValueError if x is negative or non-integral.\n",
            "    \n",
            "    floor(x, /)\n",
            "        Return the floor of x as an Integral.\n",
            "        \n",
            "        This is the largest integer <= x.\n",
            "    \n",
            "    fmod(x, y, /)\n",
            "        Return fmod(x, y), according to platform C.\n",
            "        \n",
            "        x % y may differ.\n",
            "    \n",
            "    frexp(x, /)\n",
            "        Return the mantissa and exponent of x, as pair (m, e).\n",
            "        \n",
            "        m is a float and e is an int, such that x = m * 2.**e.\n",
            "        If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.\n",
            "    \n",
            "    fsum(seq, /)\n",
            "        Return an accurate floating point sum of values in the iterable seq.\n",
            "        \n",
            "        Assumes IEEE-754 floating point arithmetic.\n",
            "    \n",
            "    gamma(x, /)\n",
            "        Gamma function at x.\n",
            "    \n",
            "    gcd(x, y, /)\n",
            "        greatest common divisor of x and y\n",
            "    \n",
            "    hypot(...)\n",
            "        hypot(*coordinates) -> value\n",
            "        \n",
            "        Multidimensional Euclidean distance from the origin to a point.\n",
            "        \n",
            "        Roughly equivalent to:\n",
            "            sqrt(sum(x**2 for x in coordinates))\n",
            "        \n",
            "        For a two dimensional point (x, y), gives the hypotenuse\n",
            "        using the Pythagorean theorem:  sqrt(x*x + y*y).\n",
            "        \n",
            "        For example, the hypotenuse of a 3/4/5 right triangle is:\n",
            "        \n",
            "            >>> hypot(3.0, 4.0)\n",
            "            5.0\n",
            "    \n",
            "    isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)\n",
            "        Determine whether two floating point numbers are close in value.\n",
            "        \n",
            "          rel_tol\n",
            "            maximum difference for being considered \"close\", relative to the\n",
            "            magnitude of the input values\n",
            "          abs_tol\n",
            "            maximum difference for being considered \"close\", regardless of the\n",
            "            magnitude of the input values\n",
            "        \n",
            "        Return True if a is close in value to b, and False otherwise.\n",
            "        \n",
            "        For the values to be considered close, the difference between them\n",
            "        must be smaller than at least one of the tolerances.\n",
            "        \n",
            "        -inf, inf and NaN behave similarly to the IEEE 754 Standard.  That\n",
            "        is, NaN is not close to anything, even itself.  inf and -inf are\n",
            "        only close to themselves.\n",
            "    \n",
            "    isfinite(x, /)\n",
            "        Return True if x is neither an infinity nor a NaN, and False otherwise.\n",
            "    \n",
            "    isinf(x, /)\n",
            "        Return True if x is a positive or negative infinity, and False otherwise.\n",
            "    \n",
            "    isnan(x, /)\n",
            "        Return True if x is a NaN (not a number), and False otherwise.\n",
            "    \n",
            "    isqrt(n, /)\n",
            "        Return the integer part of the square root of the input.\n",
            "    \n",
            "    ldexp(x, i, /)\n",
            "        Return x * (2**i).\n",
            "        \n",
            "        This is essentially the inverse of frexp().\n",
            "    \n",
            "    lgamma(x, /)\n",
            "        Natural logarithm of absolute value of Gamma function at x.\n",
            "    \n",
            "    log(...)\n",
            "        log(x, [base=math.e])\n",
            "        Return the logarithm of x to the given base.\n",
            "        \n",
            "        If the base not specified, returns the natural logarithm (base e) of x.\n",
            "    \n",
            "    log10(x, /)\n",
            "        Return the base 10 logarithm of x.\n",
            "    \n",
            "    log1p(x, /)\n",
            "        Return the natural logarithm of 1+x (base e).\n",
            "        \n",
            "        The result is computed in a way which is accurate for x near zero.\n",
            "    \n",
            "    log2(x, /)\n",
            "        Return the base 2 logarithm of x.\n",
            "    \n",
            "    modf(x, /)\n",
            "        Return the fractional and integer parts of x.\n",
            "        \n",
            "        Both results carry the sign of x and are floats.\n",
            "    \n",
            "    perm(n, k=None, /)\n",
            "        Number of ways to choose k items from n items without repetition and with order.\n",
            "        \n",
            "        Evaluates to n! / (n - k)! when k <= n and evaluates\n",
            "        to zero when k > n.\n",
            "        \n",
            "        If k is not specified or is None, then k defaults to n\n",
            "        and the function returns n!.\n",
            "        \n",
            "        Raises TypeError if either of the arguments are not integers.\n",
            "        Raises ValueError if either of the arguments are negative.\n",
            "    \n",
            "    pow(x, y, /)\n",
            "        Return x**y (x to the power of y).\n",
            "    \n",
            "    prod(iterable, /, *, start=1)\n",
            "        Calculate the product of all the elements in the input iterable.\n",
            "        \n",
            "        The default start value for the product is 1.\n",
            "        \n",
            "        When the iterable is empty, return the start value.  This function is\n",
            "        intended specifically for use with numeric values and may reject\n",
            "        non-numeric types.\n",
            "    \n",
            "    radians(x, /)\n",
            "        Convert angle x from degrees to radians.\n",
            "    \n",
            "    remainder(x, y, /)\n",
            "        Difference between x and the closest integer multiple of y.\n",
            "        \n",
            "        Return x - n*y where n*y is the closest integer multiple of y.\n",
            "        In the case where x is exactly halfway between two multiples of\n",
            "        y, the nearest even value of n is used. The result is always exact.\n",
            "    \n",
            "    sin(x, /)\n",
            "        Return the sine of x (measured in radians).\n",
            "    \n",
            "    sinh(x, /)\n",
            "        Return the hyperbolic sine of x.\n",
            "    \n",
            "    sqrt(x, /)\n",
            "        Return the square root of x.\n",
            "    \n",
            "    tan(x, /)\n",
            "        Return the tangent of x (measured in radians).\n",
            "    \n",
            "    tanh(x, /)\n",
            "        Return the hyperbolic tangent of x.\n",
            "    \n",
            "    trunc(x, /)\n",
            "        Truncates the Real x to the nearest Integral toward 0.\n",
            "        \n",
            "        Uses the __trunc__ magic method.\n",
            "\n",
            "DATA\n",
            "    e = 2.718281828459045\n",
            "    inf = inf\n",
            "    nan = nan\n",
            "    pi = 3.141592653589793\n",
            "    tau = 6.283185307179586\n",
            "\n",
            "FILE\n",
            "    (built-in)\n",
            "\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%%writefile cal.py\n",
        "def add(x,y):\n",
        "   '''this function is use to add two number '''\n",
        "    return x+y\n",
        "def sub(x,y):\n",
        "    '''this function is use to sub two number '''\n",
        "    return x-y\n",
        "def mul(x,y):\n",
        "    '''this function is use to mul two number '''\n",
        "    return x*y\n",
        "def div(x,y):\n",
        "    '''this function is use to div two number '''\n",
        "    return x/y        \n",
        "if __name__==\"__main__\":\n",
        "  '''this is a cal function\n",
        "      you can perform \n",
        "      add() -- addition\n",
        "      sub()  --substracion\n",
        "      mul() --multplication\n",
        "      div() --division '''"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "b7wrHEx3Aq5o",
        "outputId": "024a75cc-2587-4bfa-9803-03c8a3359ccb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Overwriting cal.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import cal\n",
        "print(cal.add(1,2))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LSQvLoTlCxp5",
        "outputId": "a23f4b77-5852-4858-c3fb-7e88b5d0bd9a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import cal\n",
        "help(cal)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "roYaXzNZC8Xv",
        "outputId": "8cdcfb53-e09e-4fff-bb97-4918b32c566f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Help on module cal:\n",
            "\n",
            "NAME\n",
            "    cal\n",
            "\n",
            "FUNCTIONS\n",
            "    add(x, y)\n",
            "    \n",
            "    div(x, y)\n",
            "    \n",
            "    mul(x, y)\n",
            "    \n",
            "    sub(x, y)\n",
            "\n",
            "FILE\n",
            "    /content/cal.py\n",
            "\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "''' create a python module all the function create by you'''"
      ],
      "metadata": {
        "id": "NPiv9WNdE0J9",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 36
        },
        "outputId": "5980882c-a6b7-4fa0-a54c-2a5d29dcb54d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "' create a python module all the function create by you'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#PYTHON CLASS"
      ],
      "metadata": {
        "id": "BWcs92bJ2kWo"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "The __init__() Function\n",
        "The examples above are classes and objects in their simplest form, and are not really useful in real life applications.\n",
        "\n",
        "To understand the meaning of classes we have to understand the built-in __init__() function.\n",
        "\n",
        "All classes have a function called __init__(), which is always executed when the class is being initiated.\n",
        "\n",
        "Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is"
      ],
      "metadata": {
        "id": "UU9nrG_22osc"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class students:\n",
        "    college= \"sit\"\n",
        "    def __init__(self):\n",
        "      self.sem = \"I\"\n",
        "      self.strength = 66\n",
        "      self.section = \"c\"\n",
        "    def Branch(self):\n",
        "      print(\"This is CSE\"+self.sem+\"semester\")\n",
        "  \n",
        "rohit = students()\n",
        "rohit.section"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 36
        },
        "id": "E4zbjH4phibc",
        "outputId": "7fe22768-d438-4b7b-db3b-958f1bf1ed95"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'c'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "The __str__() Function\n",
        "The __str__() function controls what should be returned when the class object is represented as a string.\n",
        "\n",
        "If the __str__() function is not set, the string representation of the object is returned:"
      ],
      "metadata": {
        "id": "o8ATfgqr3aLJ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class Person:\n",
        "  def __init__(self, name, age):\n",
        "    self.name = name\n",
        "    self.age = age\n",
        "\n",
        "p1 = Person(\"John\", 36)\n",
        "\n",
        "print(p1)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dTju3gsA3dCZ",
        "outputId": "16af247c-29d5-497f-c56b-ddbdaae6438f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<__main__.Person object at 0x7f8f713b3a90>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "INHERITANCE:\n",
        "it is a feature or a process in which ,new classes are created form the existing classes."
      ],
      "metadata": {
        "id": "yrZuCbnf44pW"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class student:\n",
        "    domain = \"btech\"\n",
        "    def display(self):\n",
        "      print(\"the domain is:\",self.domain)\n",
        "students = student()"
      ],
      "metadata": {
        "id": "wnoxyCS73qzN"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "students.display()  "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dXgWay6g57lS",
        "outputId": "c127fb64-ef80-494a-8ccd-d87695de4129"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "the domain is: btech\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "class siustudent:\n",
        "  domain = \"btech\"\n",
        "  def __init__(self,section=c,prn):\n",
        "    self.section = section\n",
        "    self.prn = prn\n",
        "  def display(self):\n",
        "    print(\"the department :\",self.domain)\n",
        "    print(\"your section is :\",self.section)\n",
        "    print(\"your prn is :\",self.prn)  \n",
        "rohit = siustudent(\"c\",22070521075)\n",
        "rohit.display()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 130
        },
        "id": "Q0AfoZi16WI-",
        "outputId": "5543bf18-1d6c-419b-a49b-9597ef61f09d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "SyntaxError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-27-5236fd55482e>\"\u001b[0;36m, line \u001b[0;32m3\u001b[0m\n\u001b[0;31m    def __init__(self,section=c,prn):\u001b[0m\n\u001b[0m                 ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m non-default argument follows default argument\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "class siustudents(siustudent):\n",
        "    qualification = \"btech\"\n",
        "    def __init__(self,class_number):\n",
        "      self.branch = \"cse\"\n",
        "      self.class_number  = class_number\n",
        "    def diplay(self):\n",
        "      print(\"the qualification :\",self.qualification)\n",
        "      print(\"branch is :\",self.branch)\n",
        "      print(\"class room\",self.room_number)\n",
        "student =siustudents(103)    "
      ],
      "metadata": {
        "id": "6KvbR51y-Haz"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "student.display()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 304
        },
        "id": "NenD11xRBKlA",
        "outputId": "0deee530-89b8-4b7c-fcf9-ad84e1d5983d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "the department : btech\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "AttributeError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-29-7ef9876fe1e1>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mstudent\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdisplay\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;32m<ipython-input-24-b3fa6684d743>\u001b[0m in \u001b[0;36mdisplay\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m      6\u001b[0m   \u001b[0;32mdef\u001b[0m \u001b[0mdisplay\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      7\u001b[0m     \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"the department :\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdomain\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 8\u001b[0;31m     \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"your section is :\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msection\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      9\u001b[0m     \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"your prn is :\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mprn\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     10\u001b[0m \u001b[0mrohit\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0msiustudent\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"c\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m22070521075\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mAttributeError\u001b[0m: 'siustudents' object has no attribute 'section'"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "recursion:\n",
        "function call itself"
      ],
      "metadata": {
        "id": "B0SNLR-OB4RY"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def fun(n):\n",
        "  if n == 1:\n",
        "    return 1\n",
        "  else:\n",
        "    return 2+fun(n-1) \n",
        "if __name__==\"__main__\":\n",
        "    print(fun(4))     "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pZ8xgNeiCB3D",
        "outputId": "6704ba0d-57a1-4745-f035-0c0fb6cfe38f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "7\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def fact(n):\n",
        "  if n == 1:\n",
        "    return 1\n",
        "  else:\n",
        "    return n*fact(n-1)\n",
        "fact(5)      "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "80LLtUE1DV1U",
        "outputId": "eb364395-ae93-4de4-b9f6-8c2edfe66538"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "120"
            ]
          },
          "metadata": {},
          "execution_count": 34
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#write a program to find sum of digit of user given number using recursion\n",
        "def sumofdigit(n):\n",
        "   if n == 0:\n",
        "      return 0\n",
        "   else:\n",
        "      return n%10 + sumofdigit(n//10)    \n",
        "\n",
        "sumofdigit(192012903710237014790)       "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JaX_pROWDyPH",
        "outputId": "dff43680-138d-43c3-a4ac-4cb5a6853b6f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "68"
            ]
          },
          "metadata": {},
          "execution_count": 41
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def sumofdigit(n):\n",
        "  print(0) if n == 0 else print(n%10 + sumofdigit(n//10))   \n",
        "sumofdigit(10)  "
      ],
      "metadata": {
        "id": "RqU8j5d3Ejmc"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#wap to create a class animal number of eyes ,leg , tail,and bhaivour ..subclass bird to over write the categare "
      ],
      "metadata": {
        "id": "YONep26nJ_be"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "class animal:\n",
        "     def __init__(self,neye,nleg,ntail,behaviour):\n",
        "       "
      ],
      "metadata": {
        "id": "VuEwrQj8Kx9j"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "%%writefile fibo.py\n",
        "\n",
        "def fibb(n):\n",
        "   a,b =0,1  \n",
        "   while a < n:\n",
        "      print(a,end=\" \")\n",
        "      a,b =b,a+b\n",
        "if __name__==\"__main__\":\n",
        "    stop = int(input(\"enter range:\"))\n",
        "    fibb(stop)"
      ],
      "metadata": {
        "id": "y5WgDXD7KxFy",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "eea0c5ae-cb16-405b-d8ba-9431d940b40a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Overwriting fibo.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import fibo\n",
        "fibo.fibb(10)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HDKIrrvrVpvU",
        "outputId": "33c0caf2-65d5-42a1-adf2-bafbe687a2dc"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0\n",
            "1\n",
            "1\n",
            "2\n",
            "3\n",
            "5\n",
            "8\n",
            "13\n",
            "21\n",
            "34\n"
          ]
        }
      ]
    }
  ]
}