/********************************************************************************
** Form generated from reading UI file 'loginC11426.ui'
**
** Created by: Qt User Interface Compiler version 4.8.7
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef LOGINC11426_H
#define LOGINC11426_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QDialog>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QLineEdit>
#include <QtGui/QPushButton>

QT_BEGIN_NAMESPACE

class Ui_AcessControl
{
public:
    QLabel *UserName;
    QLabel *label_2;
    QLineEdit *lineEdit;
    QLineEdit *lineEdit_2;
    QLabel *label;
    QPushButton *pushButton;
    QPushButton *pushButton_2;

    void setupUi(QDialog *AcessControl)
    {
        if (AcessControl->objectName().isEmpty())
            AcessControl->setObjectName(QString::fromUtf8("AcessControl"));
        AcessControl->resize(340, 240);
        UserName = new QLabel(AcessControl);
        UserName->setObjectName(QString::fromUtf8("UserName"));
        UserName->setGeometry(QRect(50, 70, 66, 17));
        label_2 = new QLabel(AcessControl);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setGeometry(QRect(50, 110, 66, 17));
        lineEdit = new QLineEdit(AcessControl);
        lineEdit->setObjectName(QString::fromUtf8("lineEdit"));
        lineEdit->setGeometry(QRect(120, 70, 113, 21));
        lineEdit_2 = new QLineEdit(AcessControl);
        lineEdit_2->setObjectName(QString::fromUtf8("lineEdit_2"));
        lineEdit_2->setGeometry(QRect(120, 110, 113, 21));
        lineEdit_2->setMaxLength(1);
        label = new QLabel(AcessControl);
        label->setObjectName(QString::fromUtf8("label"));
        label->setGeometry(QRect(30, 20, 261, 17));
        pushButton = new QPushButton(AcessControl);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));
        pushButton->setGeometry(QRect(230, 180, 97, 27));
        pushButton_2 = new QPushButton(AcessControl);
        pushButton_2->setObjectName(QString::fromUtf8("pushButton_2"));
        pushButton_2->setGeometry(QRect(110, 180, 97, 27));

        retranslateUi(AcessControl);

        QMetaObject::connectSlotsByName(AcessControl);
    } // setupUi

    void retranslateUi(QDialog *AcessControl)
    {
        AcessControl->setWindowTitle(QApplication::translate("AcessControl", "Dialog", 0, QApplication::UnicodeUTF8));
        UserName->setText(QApplication::translate("AcessControl", "Username", 0, QApplication::UnicodeUTF8));
        label_2->setText(QApplication::translate("AcessControl", "Password", 0, QApplication::UnicodeUTF8));
        lineEdit_2->setInputMask(QApplication::translate("AcessControl", "*; ", 0, QApplication::UnicodeUTF8));
        lineEdit_2->setText(QApplication::translate("AcessControl", "*", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("AcessControl", "Please Login To Acess This Application", 0, QApplication::UnicodeUTF8));
        pushButton->setText(QApplication::translate("AcessControl", "Login", 0, QApplication::UnicodeUTF8));
#ifndef QT_NO_ACCESSIBILITY
        pushButton_2->setAccessibleName(QApplication::translate("AcessControl", "bcancel", 0, QApplication::UnicodeUTF8));
#endif // QT_NO_ACCESSIBILITY
        pushButton_2->setText(QApplication::translate("AcessControl", "Cancel", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class AcessControl: public Ui_AcessControl {};
} // namespace Ui

QT_END_NAMESPACE

#endif // LOGINC11426_H
