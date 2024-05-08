print('welcome to Running from your life.\nYour misssion is to dont die.')
print('''

                               ________________
                          ____/ (  (    )   )  \___
                         /( (  (  )   _    ))  )   ))
                       ((     (   )(    )  )   (   )  )
                     ((/  ( _(   )   (   _) ) (  () )  )
                    ( (  ( (_)   ((    (   )  .((_ ) .  )_
                   ( (  )    (      (  )    )   ) . ) (   )
                  (  (   (  (   ) (  _  ( _) ).  ) . ) ) ( )
                  ( (  (   ) (  )   (  ))     ) _)(   )  )  )
                 ( (  ( \ ) (    (_  ( ) ( )  )   ) )  )) ( )
                  (  (   (  (   (_ ( ) ( _    )  ) (  )  )   )
                 ( (  ( (  (  )     (_  )  ) )  _)   ) _( ( )
                  ((  (   )(    (     _    )   _) _(_ (  (_ )
                   (_((__(_(__(( ( ( |  ) ) ) )_))__))_)___)
                   ((__)        \\||lll|l||///          \_))
                            (   /(/ (  )  ) )\   )
                          (    ( ( ( | | ) ) )\   )
                           (   /(| / ( )) ) ) )) )
                         (     ( ((((_(|)_)))))     )
                          (      ||\(|(|)|/||     )
                        (        |(||(||)||||        )
                          (     //|/l|||)|\\ \     )
                        (/ / //  /|//||||\\  \ \  \ _)
-------------------------------------------------------------------------------

''')

print('You are running from a bomb, you have to run fast, but be careful to dont fall!\n')
a1 = input('You have to turn left or right, where you gonna turn? ')
a1 = a1.lower()
if a1 == 'left':
    print('You fell into a hole, you dead now :(')
elif a1 == 'right':
    a2 = input('You have to jump or go under a fence, what you gonna do? ')
    if a2 == 'jump':
        print('You broke your leg when you tried to jumo, you are dead now :( ')
    elif a2 == 'go under' or 'go under the fence':
        a3 = input('You almost in the safe zone, there is a river, you have to either swim, go around the river or wait, what you gonna do? ')
        if a3 == 'swim':
                print('YAY you made it, now you are safe!\n YOU WIN.')
                print('''

     .-.                                    ,-.
  .-(   )-.                              ,-(   )-.
 (     __) )-.                        ,-(_      __)
  `-(       __)                      (_    )  __)-'
    `(____)-',                        `-(____)-'
  - -  :   :  - -
      / `-' \
    ,    |   .
         .                         _
                                  >')
               _   /              (\\         (W)
              =') //               = \     -. `|'
               ))////)             = ,-      \(| ,-
              ( (///))           ( |/  _______\|/____
~~~~~~~~~~~~~~~`~~~~'~~~~~~~~~~~~~\|,-'::::::::::::::
            _                 ,----':::::::::::::::::
         {><_'c   _      _.--':MJP:::::::::::::::::::
__,'`----._,-. {><_'c  _-':::::::::::::::::::::::::::
:.:.:.:.:.:.:.\_    ,-'.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:
.:.:.:.:.:.:.:.:`--'.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.
.....................................................

''')
        elif a3 == 'go around'or 'go around it' or 'go around the river':
            print('The explosion reached to you before you could get to the other side, you are dead now :( ')
        elif a3 == 'wait':
            print('The explosion reached to you before you could get to the other side, you are dead now :( ')
        else:
            print('GAME OVER')
    else:
        print('GAME OVER')
else:
    print('GAME OVER')