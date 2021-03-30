#ifndef HOLE_H
#define HOLE_H

#include <QPushButton>

class Hole : public QPushButton
{
    Q_OBJECT
    Q_PROPERTY(int row READ row WRITE setRow)
    Q_PROPERTY(int col READ col WRITE setCol)
    Q_PROPERTY(Hole::State state READ state WRITE setState NOTIFY stateChanged)
public:
    enum State{
        Empty,
        Red,
        Blue,
        Selectable
    };
    Q_ENUM(State)
    explicit Hole(QWidget *parent = nullptr);
    virtual ~Hole();

    int row() const {return m_row;}
    void setRow(int row) {m_row = row;}

    int col() const {return m_col;}
    void setCol(int col) {m_col = col;}

    Hole::State state() const{return m_state;}
    void setState(Hole::State state);

signals:
    void stateChanged(Hole::State old_state, Hole::State new_state);

private:
    int m_row;
    int m_col;
    Hole::State m_state;

    static QPixmap state2pixmap(Hole::State state);

private slots:
    void updateHole(Hole::State old_state, Hole::State new_state);

};


#endif // HOLE_H
