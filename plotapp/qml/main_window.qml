import QtQuick 2.6
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.2

import QtQuickFigureCanvas 1.0

ApplicationWindow
{
    //title of the application
    title: qsTr("Sample Plot App")
    width: 640
    height: 480
    color: "whitesmoke"

    onClosing: main.shutdown()

    RowLayout
    {
        id: mainLayout
        anchors.fill: parent
        spacing: 10

//        Rectangle {
//            id: placeholder
//            color: 'red'
//            Layout.fillHeight: true
//            Layout.fillWidth: true
//        }

        FigureCanvas {
                id: mplView
                objectName : "figure"
                Layout.fillHeight: true
                Layout.fillWidth: true
            }

        Button {
            id: generateButton
            text: "Generate"
            onClicked: main.generate_data()
        }
    }  // ColumnLayout
}  // ApplicationWindow
