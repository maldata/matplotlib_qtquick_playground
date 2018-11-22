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
//    Component.onCompleted: connectToSignals()

//    function connectToSignals() {
//        main.screen_changed.connect(mainWindow.changeScreen);
//        main.engines_initialized.connect(mainWindow.enginesInitialized);
//    }

    // The Keys property can't be attached to anything that doesn't descend from Item,
    // and apparently ApplicationWindow doesn't. So, let's just wrap everything in Item.
    Item {
        anchors.fill: parent
        focus: true
        Keys.onPressed: {
            if (event.key === Qt.Key_1)
            {
                onPressed: main.changeContent(1)
            }
            else if (event.key === Qt.Key_2)
            {
                onPressed: main.changeContent(2)
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
                    onPressed: main.changeContent(1)
                }

                Button {
                    id: buttonScreen2
                    text: "Screen 2"
                    Layout.fillWidth: true
                    onPressed: main.changeContent(2)
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

//    Item {
//        anchors.fill: parent
//        focus: true
//        Keys.onPressed: {
//            if (event.key === Qt.Key_F2) {
//                main.change_screen(600)
//            } else if (event.key === Qt.Key_F3) {
//                diagnostics.visible = !diagnostics.visible
//            }
//        }

//        RowLayout {
//            anchors.fill: parent
//            spacing: 0

//            Rectangle {
//                Layout.fillHeight: true
//                Layout.minimumWidth: Style.sideBarWidth
//                Layout.maximumWidth: Style.sideBarWidth
//                color: Style.darkBlueBackgroundColor

//                Loader {
//                    id: sideBarLoader
//                    anchors.left: parent.left
//                    anchors.right: parent.right
//                }
//            }

//            Rectangle {
//                Layout.fillHeight: true
//                Layout.preferredWidth: 3
//                color: Style.blueBorderColor
//            }

//            Rectangle {
//                Layout.fillWidth: true
//                Layout.fillHeight: true

//                Rectangle {
//                    id: tabBar
//                    anchors.top: parent.top
//                    width: parent.width
//                    height: Style.topBarHeight
//                    color: Style.darkGrayBackgroundColor

//                    RowLayout {
//                        anchors.fill: parent
//                        anchors.margins: Style.standardMargin

//                        Repeater {
//                            model: [
//                                // The ID of each screen is defined in screenmap.py
//                                { id: 100, text: qsTr("Overview") },
//                                { id: 200, text: qsTr("Systems") },
//                                { id: 300, text: qsTr("Graphs") }
//                            ]

//                            PageButton {
//                                Layout.alignment: Qt.AlignHCenter
//                                text: modelData.text
//                                active: Math.floor(main.active_id/100)*100 === modelData.id  // a tab is considered active if any of its subscreens are active
//                                onClicked: main.change_screen(modelData.id)
//                            }
//                        }

//                        PageButton {
//                            Layout.alignment: Qt.AlignHCenter
//                            text: qsTr("Alarms")
//                            active: Math.floor(main.active_id/100)*100 === 400  // a tab is considered active if any of its subscreens are active
//                            onClicked: main.change_screen(400)

//                            // Pulse/color alarm tab based on alarm status
//                            alertPulse: main.alert_pulse
//                            alertColor: main.alert_color
//                        }

//                        PageButton {
//                            Layout.alignment: Qt.AlignHCenter
//                            width: height
//                            imageSource: "../images/settings.png"
//                            active: Math.floor(main.active_id/100)*100 === 800 // a tab is considered active if any of its subscreens are active
//                            onClicked: main.change_screen(800)
//                        }
//                    }
//                }

//                Rectangle {
//                    id: tabBarBorder
//                    anchors.top: tabBar.bottom
//                    anchors.left: parent.left
//                    anchors.right: parent.right
//                    height: 3
//                    color: Style.blueBorderColor
//                }

//                Loader {
//                    id: screenLoader
//                    clip: true
//                    anchors.top: tabBarBorder.bottom
//                    anchors.left: parent.left
//                    anchors.right: parent.right
//                    anchors.bottom: parent.bottom
//                }
//            }
//        }

//        RowLayout {
//            id: diagnostics
//            visible: false
//            anchors.top: parent.top
//            anchors.topMargin: 0
//            anchors.left: parent.left
//            anchors.leftMargin: Style.standardMargin
//            spacing: Style.standardMargin * 2

//            Text {
//                font.pixelSize: 8
//                color: "white"
//                text: main.app_version
//            }
//        }
//    }
//}
