# Expense Manager

This project is a command-line based Expense Manager written in Python. It allows users to register, log in, manage expenses, and update their income. User passwords are encrypted and stored securely.

## Features

- **User Registration and Login:** Securely register and log in users with encrypted passwords.
- **Add Expense:** Add new expenses to the user's expense record.
- **Show Expense:** Display all expenses recorded by the user.
- **Update Income:** Update the user's income/salary information.
- **Show Income:** Display the current income/salary of the user.
- **Show Report:** Generate a report of the user's income and expenses.

## Setup

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/yourusername/expense-manager.git
   cd expense-manager
   ```
2. **Install Dependencies:**
    Ensure you have Python installed (version 3.6 or higher). This project uses standard Python libraries, so no additional dependencies are required.
3. **Create Required CSV Files:**
    Create users.csv and auth.csv files in the project directory.
    *users.csv*
    ```csv
    username,password,salary
    ```
    *auth.csv*
    ```csv
    A,H
    B,i
    C,e
    D,$
    E,1
    F,0
    G,f
    H,Q
    I,A
    J,w
    K,v
    L,j
    M,Z
    N,>
    O,S
    P,)
    Q,E
    R,L
    S,J
    T,F
    U,C
    V,2
    W,O
    X,B
    Y,I
    Z,D
    a,z
    b,s
    c,9
    d,7
    e,+
    f,x
    g,&
    h,@
    i,a
    j,{
    k,V
    l,<
    m,n
    n,N
    o,4
    p,(
    q,#
    r,P
    s,m
    t,|
    u,?
    v,[
    w,W
    x,`
    y,o
    z,:
    0,_
    1,b
    2,;
    3,K
    4,*
    5,t
    6,l
    7,]
    8,U
    9,d
    !,.
    @,5
    #,k
    $,!
    %,p
    ^,g
    &,X
    *,3
    (,^
    ),r
    -,T
    _,u
    =,8
    +,/
    [,c
    ],Y
    {,~
    },h
    |,6
    ;,q
    :,R
    .,%
    /,G
    <,}
    >,-
    ?,=
    `,y
    ~,M

    ```
## Usage
    Run the script to start the Expense Manager:
    ```sh
    python main.py
    ```

## Register a New User
    1. When prompted, enter your username.
    2. If you are a new user, create a password and enter your salary.

## Login as an Existing User
    1. When prompted, enter your username.
    2. If you are an existing user, enter your password to log in.

## Manage Expenses and Income
    Once logged in, follow the on-screen menu to add expenses, show expenses, update income, show income, or exit the program.

## FIle Structure
    ```css
       expense-manager/
    │
    ├── auth.py
    ├── expense.py
    ├── income.py
    ├── main.py
    ├── auth.csv
    ├── users.csv
    └── README.md
    ```



