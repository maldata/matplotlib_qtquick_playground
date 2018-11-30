import QtQuick 2.7
import QtQuick.Controls 2.1
import QtQuick.Layouts 1.3

import Matplot 1.0

import "../styles"

ColumnLayout {
    anchors.fill: parent

    Label {
        text: "Here's a plot!"
    }

    Matplot {
        Layout.fillHeight: true
        Layout.fillWidth: true
    }
}
