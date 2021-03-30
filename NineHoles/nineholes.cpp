#include "nineholes.h"
#include "ui_nineholes.h"

#include <cmath>
#include <QDebug>
#include <QSignalMapper>
#include <QMessageBox>

const int maxTurns = 40; //Decidi declarar um empate caso o jogo se prolongue
int winner;
int turn = 0;
bool player = true;
bool battle = false;
int initialPieces = 0;
int table[3][3] ={0}; //Auxiliar "abstrato" do tabuleiro do jogo
int flag = 0; /*variável auxiliar para saber a cor do jogador atual, não estou usando o player pq fui burro e declarei como booleano
                fiquei com preguiça de corrigir meu erro*/
int previousRow, previousCol;
bool standby = true;

NineHoles::NineHoles(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::NineHoles)
{
    ui->setupUi(this);

    this->adjustSize();
    this->setFixedSize(this->size());


    QObject::connect(ui->actionSair, SIGNAL(triggered(bool)), qApp, SLOT(quit()));
    QObject::connect(ui->actionNovo, SIGNAL(triggered(bool)), this, SLOT(reset()));
    QObject::connect(ui->actionAjuda, SIGNAL(triggered(bool)), this, SLOT(showAbout()));
    QSignalMapper* map = new QSignalMapper(this);

    for(int id = 0; id < 9; id++)
    {
        int r = id/3;
        int c = id%3;
//        qDebug() << r;
//        qDebug() << c;
//        qDebug() << "\n";

        Hole* hole = this->findChild<Hole*>(QString("hole%1%2").arg(r).arg(c));
//        qDebug() << hole->row();
//        qDebug() << hole->col();


        Q_ASSERT(hole!=0);

        m_holes[id] = hole;
        map->setMapping(hole, id);
        QObject::connect(hole, SIGNAL(clicked(bool)), map, SLOT(map()));
    }
    QObject::connect(map, SIGNAL(mapped(int)), this, SLOT(play(int)));

}

NineHoles::~NineHoles()
{
    delete ui;
}


void NineHoles::play(int id)
{
   Hole* hole = m_holes[id];
     //qDebug() << "row: " << hole->row();
     //qDebug() << "col: " << hole->col();
//   qDebug() << "\n";
     //qDebug()<<hole;
   int row = hole->row();
   int col = hole->col();

   //batalha quer dizer que as peças iniciais foram colocadas no tabuleiro e então começa a fase de movimentálas
   game(row, col, hole);


   winner = checkWin();
   if(winner !=0 ){
       if(winner == 1){
           //qDebug()<<"Jogador Vermelho Venceu";
       }
       if(winner == 2){
           //qDebug()<<"Jogador Azul Venceu";
       }
       showGameOver();
   }
   if(turn == maxTurns){
       winner = 3;
       showGameOver();
   }
   turn ++;
}


void NineHoles::reset()
{
    for(int id = 0; id < 9; id++){
        Hole* hole = m_holes[id];
        hole->setState(Hole::Empty);
    }
    player = true;
    initialPieces = 0;
    battle = false;
    standby = true;
    turn = 0;
    flag = 0;

    for(int i=0; i<3; i++){
        for(int j=0; j<3;j++){
            table[i][j]=0;
        }
    }
}


int NineHoles::checkWin(){
    for(int i=0; i<3; i++){
        if(table[i][0]==1 && table[i][1]==1 && table[i][2]==1){
            return 1;
        }
        if(table[i][0]==2 && table[i][1]==2 && table[i][2]==2){
            return 2;
        }
        if(table[0][i]==1 && table[1][i]==1 && table[2][i]==1){
            return 1;
        }
        if(table[0][i]==2 && table[1][i]==2 && table[2][i]==2){
            return 2;
        }
    }

     return 0;
}


//checa se a posição onde jogador está tentando colocar a peça é adjacente a peça removida(somente na horizontal ou vertical)
bool NineHoles::validMove(int row, int col, int prevRow, int prevCol ){

    if(abs(row - prevRow)==1 /*| abs(row - prevRow)==0*/){
       if(abs(col - prevCol)==0){
           return true;
       }
   }else if (abs(col-prevCol)==1 /*| abs(row - prevRow)==0*/){
       if(abs(row-prevRow)==0){
           return true;
       }
   }return false;


}


void NineHoles::showAbout()
{
    QMessageBox::information(this, tr("Sobre"), tr("Nine Holes\n\nLara Galvani & Fulvio Taroni\nfulviotaroni@gmail.com\nlaragalvanim@gmail.com"));
}


void NineHoles::showGameOver() {
    if (winner == 1)
        QMessageBox::information(this, tr("Vencedor"), tr("Parabéns, o jogador vermelho venceu."));
    if (winner == 2)
        QMessageBox::information(this, tr("Vencedor"), tr("Parabéns, o jogador azul venceu."));
    if (winner == 3)
        QMessageBox::information(this, tr("Empate"), tr("Os jogadores empataram."));
};


//controle dos eventos no jogo
void NineHoles::game(int row, int col, Hole* hole){
    //batalha quer dizer que as peças iniciais foram colocadas no tabuleiro e então começa a fase de movimentálas
    if(battle == false){
        if(table[row][col]==0){
            //qDebug()<<initialPieces;
            if(player == true && initialPieces <= 6){
              hole->setState(Hole::Red);
              table[row][col] = 1;
              initialPieces++;
              //qDebug()<<initialPieces;
            }

            if(player == false && initialPieces <= 6){
               hole->setState(Hole::Blue);
               table[row][col] = 2;
               initialPieces++;
               //qDebug()<<initialPieces;
            }


            if(initialPieces >= 6){
                //qDebug()<<"oi";
                battle = true;
            }
            player = !player;
        }
    }else{

    //standby quer dizer o momento em que uma peça é removida do jogo e está aguardando uma nova posição para ela
    if(battle == true){
         flag = 2 - player;
         if (standby == true){
             if (table[row][col] == flag){
                 table[row][col] = 0;
                 hole->setState(Hole::Empty);
                 previousRow = row;
                 previousCol = col;
                 standby = !standby;
              }
         }
         else{
             //qDebug()<<((abs(previousRow-row) == 1)^(abs(previousCol-col)==1));
             //qDebug()<<abs(previousRow-row);
             if ((table[row][col]==0) && validMove(row, col, previousRow, previousCol)){
                 if (player == false){
                     hole->setState(Hole::Blue);
                     table[row][col] = 2;
                     standby = !standby;
                 }

                 else{
                     hole->setState(Hole::Red);
                     table[row][col] = 1;
                     standby = !standby;
                 }
                 player = !player;
 //           if (col == previousCol && row == previousCol){
 //                  player = !player;
 //             }
            }
         }
    }
 }
}



