import QtQuick 2.7
import QtQuick.Controls 2.1
import QtQuick.Layouts 1.3

import "../styles"

ColumnLayout {
    anchors.fill: parent

    Label {
        text: "Here's a plot!"
    }

    // We'll replace this with our plot control.
    Item {
    	 Layout.fillHeight: true
    }
}
