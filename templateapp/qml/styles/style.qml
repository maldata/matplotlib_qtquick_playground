pragma Singleton
import QtQuick 2.7

QtObject {
    property int windowHeight: 480
    property int windowWidth: 720

    property int sidebarWidth: 200
    property int contentMinWidth: windowWidth - sidebarWidth
}
