tcl86t.dll      tk86t.dll       tk              __splash              �  �  �   �   Xtk\ttk\cursors.tcl tk86t.dll tk\tk.tcl tk\license.terms tk\text.tcl tk\ttk\ttk.tcl tk\ttk\utils.tcl VCRUNTIME140.dll tcl86t.dll tk\ttk\fonts.tcl proc _ipc_server {channel clientaddr clientport} {
set client_name [format <%s:%d> $clientaddr $clientport]
chan configure $channel \
-buffering none \
-encoding utf-8 \
-eofchar \x04 \
-translation cr
chan event $channel readable [list _ipc_caller $channel $client_name]
}
proc _ipc_caller {channel client_name} {
chan gets $channel cmd
if {[chan eof $channel]} {
chan close $channel
exit
} elseif {![chan blocked $channel]} {
if {[string match "update_text*" $cmd]} {
global status_text
set first [expr {[string first "(" $cmd] + 1}]
set last [expr {[string last ")" $cmd] - 1}]
set status_text [string range $cmd $first $last]
}
}
}
set server_socket [socket -server _ipc_server -myaddr localhost 0]
set server_port [fconfigure $server_socket -sockname]
set env(_PYIBoot_SPLASH) [lindex $server_port 2]
image create photo splash_image
splash_image put $_image_data
unset _image_data
proc canvas_text_update {canvas tag _var - -} {
upvar $_var var
$canvas itemconfigure $tag -text $var
}
package require Tk
set image_width [image width splash_image]
set image_height [image height splash_image]
set display_width [winfo screenwidth .]
set display_height [winfo screenheight .]
set x_position [expr {int(0.5*($display_width - $image_width))}]
set y_position [expr {int(0.5*($display_height - $image_height))}]
frame .root
canvas .root.canvas \
-width $image_width \
-height $image_height \
-borderwidth 0 \
-highlightthickness 0
.root.canvas create image \
[expr {$image_width / 2}] \
[expr {$image_height / 2}] \
-image splash_image
wm attributes . -transparentcolor magenta
.root.canvas configure -background magenta
pack .root
grid .root.canvas -column 0 -row 0 -columnspan 1 -rowspan 2
wm overrideredirect . 1
wm geometry . +${x_position}+${y_position}
wm attributes . -topmost 1
raise .�PNG

   IHDR           D���   gAMA  ���a   sRGB ���    cHRM  z&  ��  �   ��  u0  �`  :�  p��Q<  %PLTE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ���`�   �tRNS >����8n���hO�w�mqo�L��M��Z�K�������*-���Є(��s,vΠ���	=&
���X��Q��b����u�V2di^���Utc1#�T]'e3��.��?�B"6�C �G���k�FI�_�l���g���;:$ya��}��[�W�p�\���/@Ɠ�1   bKGD���   	pHYs  �  ��+  AIDAT8˽RkWQ=$L�h422TL$,�I'P|�f��feaVB�!)V���_f�������jt�V��]���:w��o!!�2)!Y[�.M�.W�_�S�H������ �J�R���HA.��&Ԁ6_�[��Q��`�!�b�"���t���1cI)�Y�ܠ��.{TX�Ri�a��)A�s�c�T�D�므݃�5@����u{������Y^l �m�6��[���mŶ˖hǃu�������w�����{:����}��YW���tb��S�0N�!b�*�?���z��\�pg%��f�&���LUr>?t�"�4}�d)�p��0ݚJ��I��q�<��^.9S�� ��B��W���xא1���52A#N�/	x]��jBbj����iH`�歸(�i��ܞ���67�8mD�� �]l��*O�7��ݧ�{�)O>b���Aœ�S�xx3<Uo^�������L���W5�,��-�������R�̛���w���{��9�t���-�08\^n���if�N~�* �>YY~���@N~��
A����7���}ք��bx������K���`�   %tEXtdate:create 2018-09-26T18:15:06+02:00���   %tEXtdate:modify 2018-09-26T18:15:06+02:00��~�   FtEXtsoftware ImageMagick 6.7.8-9 2016-06-16 Q16 http://www.imagemagick.org�4�   tEXtThumb::Document::Pages 1���/   tEXtThumb::Image::height 512��PQ   tEXtThumb::Image::Width 512|�   tEXtThumb::Mimetype image/png?�VN   tEXtThumb::MTime 1537978506ϙ�"   tEXtThumb::Size 16.4KBB�V��   qtEXtThumb::URI file://./uploads/56/6QuzwkE/1580/2849830-gear-interface-multimedia-options-setting-settings_107986.png0�}    IEND�B`�