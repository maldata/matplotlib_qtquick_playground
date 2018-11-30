import QtQuick 2.7
import QtQuick.Controls 2.1
import QtQuick.Layouts 1.3

ApplicationWindow {
    id: mainWindow
    visible: true
    width: 720
    height: 480
    title: qsTr("QML Sampler")
    onClosing: main.close_application()

    RowLayout {
        anchors.fill: parent

        ColumnLayout {
            id: sideBar
            Layout.fillHeight: true
            Layout.preferredWidth: 200
            Layout.minimumWidth: 150
            Layout.maximumWidth: 350

            Button {
                id: buttonScreen1
                text: "Button 1"
                Layout.fillWidth: true
            }

            Button {
                id: buttonScreen2
                text: "Button 2"
                Layout.fillWidth: true
            }
        }

        Loader {
            id: contentAreaLoader
            Layout.fillHeight: true
            Layout.fillWidth: true
            Layout.preferredWidth: 520
            Layout.minimumWidth: 300

            source: 'loaded_content.qml'
        }
    }
}
