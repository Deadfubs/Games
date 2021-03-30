#include "hole.h"

Hole::Hole(QWidget *parent) : QPushButton(parent), m_row(0), m_col(0), m_state(Hole::Empty)
{
    QObject::connect(this, SIGNAL(stateChanged(Hole::State, Hole::State)), this, SLOT(updateHole(Hole::State, Hole::State)));
}

Hole::~Hole(){

}

void Hole::setState(Hole::State state){
    if(m_state != state){
        Hole::State old = m_state;

        m_state = state;
        emit stateChanged(old, state);
    }
}

QPixmap Hole::state2pixmap(Hole::State state){
    switch(state){
        case Hole::Empty:
            return QPixmap(":/empty");
        case Hole::Red:
            return QPixmap(":/red");
        case Hole::Blue:
            return QPixmap(":/blue");
        case Hole::Selectable:
            return QPixmap(":/selectable");
        default:
            return QPixmap();
    }
}

void Hole::updateHole(Hole::State old_state, Hole::State new_state){
    Q_UNUSED(old_state);
    this->setIcon(Hole::state2pixmap(new_state));
}

