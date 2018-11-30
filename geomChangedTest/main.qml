import QtQuick 2.7
import QtQuick.Controls 2.1
import QtQuick.Layouts 1.3

// import CustomPaintedItem 1.0

import "../qml-screens-plot/qml/styles"

ApplicationWindow {
    id: mainWindow
    visible: true
    width: Style.windowWidth
    height: Style.windowHeight
    title: qsTr("QML Sampler")
    onClosing: main.close_application()

    // The Keys property can't be attached to anything that doesn't descend from Item,
    // and apparently ApplicationWindow doesn't. So, let's just wrap everything in Item.
    Item {
        anchors.fill: parent
        focus: true

        RowLayout {
            anchors.fill: parent

            ColumnLayout {
                id: sideBar
                Layout.fillHeight: true
                Layout.preferredWidth: 200
                Layout.minimumWidth: 150

                Button {
                    id: buttonScreen1
                    text: "Screen 1"
                    Layout.fillWidth: true
                }

                Button {
                    id: buttonScreen2
                    text: "Screen 2"
                    Layout.fillWidth: true
                }
            }

            Loader {
                id: contentAreaLoader
                clip: true
                Layout.fillHeight: true
                Layout.preferredWidth: 520
                Layout.minimumWidth: 300

                source: 'loaded_content.qml'
            }
        }
    }
}
