import QtQuick 2.7
import QtQuick.Controls 2.1
import QtQuick.Layouts 1.3

import "styles"

ApplicationWindow {
    id: mainWindow
    visible: true
    width: Style.windowWidth
    height: Style.windowHeight
    title: qsTr("QML Sampler")
    onClosing: main.closeApplication()
    Component.onCompleted: connectToSignals()

    function connectToSignals()
    {
        main.active_content_changed.connect(mainWindow.update_content_area_loader);
        // main.engines_initialized.connect(mainWindow.enginesInitialized);
    }

    function update_content_area_loader(new_qml_path)
    {
        contentAreaLoader.source = new_qml_path;
    }

    // The Keys property can't be attached to anything that doesn't descend from Item,
    // and apparently ApplicationWindow doesn't. So, let's just wrap everything in Item.
    Item {
        anchors.fill: parent
        focus: true
        Keys.onPressed: {
            if (event.key === Qt.Key_1)
            {
                onPressed: main.changeContent("SCREEN1")
            }
            else if (event.key === Qt.Key_2)
            {
                onPressed: main.changeContent("SCREEN2")
            }
        }

        RowLayout {
            anchors.fill: parent

            ColumnLayout {
                Layout.fillHeight: true

                Button {
                    id: buttonScreen1
                    text: "Screen 1"
                    Layout.fillWidth: true
                    onPressed: main.changeContent("SCREEN1")
                }

                Button {
                    id: buttonScreen2
                    text: "Screen 2"
                    Layout.fillWidth: true
                    onPressed: main.changeContent("SCREEN2")
                }
            }

            Loader {
                id: contentAreaLoader
                clip: true
                Layout.fillHeight: true
                Layout.preferredWidth: Style.contentMinWidth
            }
        }
    }
}
