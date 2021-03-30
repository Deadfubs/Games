 #ifndef NINEHOLES_H
#define NINEHOLES_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class NineHoles; }
QT_END_NAMESPACE

class Hole;

class NineHoles : public QMainWindow
{
    Q_OBJECT

public:
    NineHoles(QWidget *parent = nullptr);
    ~NineHoles();

private:
    Ui::NineHoles *ui;
    Hole* m_holes[9];

    int checkWin();
    bool validMove(int row, int col, int prevRow, int prevCol);
    void game(int row, int col, Hole* hole);

private slots:
    void play(int id);
    void reset();
    void showAbout();
    void showGameOver();

};
#endif // NINEHOLES_H
