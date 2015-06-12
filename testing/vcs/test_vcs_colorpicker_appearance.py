import vcs, vtk

picker = vcs.colorpicker.ColorPicker(500, 250, None, 0)

win = picker.render_window

win.Render()
out_filter = vtk.vtkWindowToImageFilter()
out_filter.SetInput(win)

png_writer = vtk.vtkPNGWriter()
fnm = "test_vcs_colorpicker_appearance.png"
png_writer.SetFileName(fnm)
png_writer.SetInputConnection(out_filter.GetOutputPort())
png_writer.Write()

import sys, os
if len(sys.argv) > 1:
    src = sys.argv[1]
    sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
    import checkimage
    ret = checkimage.check_result_image(fnm, src, checkimage.defaultThreshold)
    sys.exit(ret)
