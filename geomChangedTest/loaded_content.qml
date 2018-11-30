import QtQuick 2.7
import QtQuick.Controls 2.1
import QtQuick.Layouts 1.3

import CustomPaintedItem 1.0

ColumnLayout {
    anchors.fill: parent

    Label {
        text: "Here's a thing!"
    }

    CustomPaintedItem {
        Layout.fillHeight: true
        Layout.fillWidth: true
    }
}
