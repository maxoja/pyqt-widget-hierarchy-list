tooltip = '''
QToolTip{
    background-color: #eff1f4;
    padding: 2px;
    border: 0px;
}
'''

selectedItem = tooltip + '''
*{
    background-color: #5b5b5b;
    /*background-color: #dbdbdb;*/
    padding: 4px;
    border: 0px;
}
'''

normalItem = tooltip + '''
*{
    background-color: #eff1f4;
    padding: 4px;
    border: 0px;
}
'''

selectedItemLabel = '''
*{
    color: white;
    padding: 0px;
}
'''

normalItemLabel = '''
*{
    color: #414142;
    padding: 0px;
}
'''

# sheet = '''
#         HierarchicalItemWidget:pressed {
#             background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(60, 186, 162, 255), stop:1 rgba(98, 211, 162, 255))
#         }
#
#         HierarchicalItemWidget {
#              background-color: #3cbaa2; border: 0.1px solid black;
#              border-radius: 0px;
#         }
#
#     '''