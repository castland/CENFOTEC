/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/GUIForms/JFrame.java to edit this template
 */
package cr.ac.ucenfotec.soft2.ui;

import cr.ac.ucenfotec.soft2.clientes.Cliente;
import cr.ac.ucenfotec.soft2.clientes.GestorClientes;
import cr.ac.ucenfotec.soft2.facturacion.HistorialVentas;
import cr.ac.ucenfotec.soft2.inventario.Inventario;
import cr.ac.ucenfotec.soft2.inventario.Producto;
import cr.ac.ucenfotec.soft2.usuarios.GestorUsuarios;
import cr.ac.ucenfotec.soft2.usuarios.Usuario;
import cr.ac.ucenfotec.soft2.ventas.Factura;

/**
 *
 * @author Carlos / Kenner
 */
public class ReportesFrame extends javax.swing.JFrame {

    private javax.swing.JFrame menuPadre;
    private static final java.util.logging.Logger logger = java.util.logging.Logger.getLogger(ReportesFrame.class.getName());
    private HistorialVentas historial;
    private final GestorUsuarios gestorUsuarios;
    private Inventario inventario;
    private Usuario usuario;
    private GestorClientes gestorClientes;

    /**
     * Creates new form ReportesFrame
     */
    public ReportesFrame(javax.swing.JFrame menuPadre, HistorialVentas historial, GestorUsuarios gestorUsuarios, Inventario inventario, Usuario usuario) {
        this.menuPadre = menuPadre;
        this.historial = historial;
        this.gestorUsuarios = gestorUsuarios;
        this.inventario = inventario;
        this.usuario = usuario;
        this.gestorClientes = new GestorClientes();
        initComponents();
    }

    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        opcionesReportesGrupoBoton = new javax.swing.ButtonGroup();
        jPanel1 = new javax.swing.JPanel();
        botonMenuPrincipal = new javax.swing.JButton();
        jPanel2 = new javax.swing.JPanel();
        ventasRadioBoton = new javax.swing.JRadioButton();
        productosRadioBoton = new javax.swing.JRadioButton();
        clientesRadioBoton = new javax.swing.JRadioButton();
        jPanel3 = new javax.swing.JPanel();
        jScrollPane1 = new javax.swing.JScrollPane();
        detallesDelReporteTextArea = new javax.swing.JTextArea();
        jPanel4 = new javax.swing.JPanel();
        fechasReportesComboBox = new javax.swing.JComboBox<>();
        jLabel1 = new javax.swing.JLabel();
        generarReporteBoton = new javax.swing.JButton();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setTitle("Panel de Reportes");
        setResizable(false);

        jPanel1.setBorder(javax.swing.BorderFactory.createTitledBorder(""));

        botonMenuPrincipal.setText("Menú Principal");
        botonMenuPrincipal.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                botonMenuPrincipalActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout jPanel1Layout = new javax.swing.GroupLayout(jPanel1);
        jPanel1.setLayout(jPanel1Layout);
        jPanel1Layout.setHorizontalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(botonMenuPrincipal)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );
        jPanel1Layout.setVerticalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(botonMenuPrincipal)
                .addContainerGap(71, Short.MAX_VALUE))
        );

        jPanel2.setBorder(javax.swing.BorderFactory.createTitledBorder("Reportes"));

        opcionesReportesGrupoBoton.add(ventasRadioBoton);
        ventasRadioBoton.setText("Ventas");

        opcionesReportesGrupoBoton.add(productosRadioBoton);
        productosRadioBoton.setText("Productos");
        productosRadioBoton.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                productosRadioBotonActionPerformed(evt);
            }
        });

        opcionesReportesGrupoBoton.add(clientesRadioBoton);
        clientesRadioBoton.setText("Clientes");

        javax.swing.GroupLayout jPanel2Layout = new javax.swing.GroupLayout(jPanel2);
        jPanel2.setLayout(jPanel2Layout);
        jPanel2Layout.setHorizontalGroup(
            jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel2Layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(ventasRadioBoton)
                    .addComponent(productosRadioBoton)
                    .addComponent(clientesRadioBoton))
                .addContainerGap(200, Short.MAX_VALUE))
        );
        jPanel2Layout.setVerticalGroup(
            jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel2Layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(ventasRadioBoton)
                .addGap(18, 18, 18)
                .addComponent(productosRadioBoton)
                .addGap(18, 18, 18)
                .addComponent(clientesRadioBoton)
                .addContainerGap(332, Short.MAX_VALUE))
        );

        jPanel3.setBorder(javax.swing.BorderFactory.createTitledBorder("Detalles del Reporte"));

        detallesDelReporteTextArea.setEditable(false);
        detallesDelReporteTextArea.setColumns(20);
        detallesDelReporteTextArea.setRows(5);
        jScrollPane1.setViewportView(detallesDelReporteTextArea);

        javax.swing.GroupLayout jPanel3Layout = new javax.swing.GroupLayout(jPanel3);
        jPanel3.setLayout(jPanel3Layout);
        jPanel3Layout.setHorizontalGroup(
            jPanel3Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel3Layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(jScrollPane1, javax.swing.GroupLayout.DEFAULT_SIZE, 652, Short.MAX_VALUE)
                .addContainerGap())
        );
        jPanel3Layout.setVerticalGroup(
            jPanel3Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel3Layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(jScrollPane1, javax.swing.GroupLayout.DEFAULT_SIZE, 280, Short.MAX_VALUE)
                .addContainerGap())
        );

        jPanel4.setBorder(javax.swing.BorderFactory.createTitledBorder("Parámetros"));

        fechasReportesComboBox.setModel(new javax.swing.DefaultComboBoxModel<>(new String[] { "Última Semana", "Último Mes", "Último Año" }));
        fechasReportesComboBox.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                fechasReportesComboBoxActionPerformed(evt);
            }
        });

        jLabel1.setText("Fecha:");

        generarReporteBoton.setText("Generar Reporte");
        generarReporteBoton.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                generarReporteBotonActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout jPanel4Layout = new javax.swing.GroupLayout(jPanel4);
        jPanel4.setLayout(jPanel4Layout);
        jPanel4Layout.setHorizontalGroup(
            jPanel4Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel4Layout.createSequentialGroup()
                .addGap(20, 20, 20)
                .addComponent(jLabel1)
                .addGap(33, 33, 33)
                .addComponent(fechasReportesComboBox, javax.swing.GroupLayout.PREFERRED_SIZE, 128, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel4Layout.createSequentialGroup()
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addComponent(generarReporteBoton)
                .addContainerGap())
        );
        jPanel4Layout.setVerticalGroup(
            jPanel4Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel4Layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(jPanel4Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(fechasReportesComboBox, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel1))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addComponent(generarReporteBoton)
                .addContainerGap())
        );

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(jPanel1, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                    .addGroup(layout.createSequentialGroup()
                        .addComponent(jPanel2, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(jPanel3, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                            .addComponent(jPanel4, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))))
                .addContainerGap())
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(jPanel1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING, false)
                    .addComponent(jPanel2, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addGroup(layout.createSequentialGroup()
                        .addComponent(jPanel4, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(jPanel3, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)))
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void generarReporteBotonActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_generarReporteBotonActionPerformed
        String fechaSeleccionada = (String) fechasReportesComboBox.getSelectedItem();
        StringBuilder reporte = new StringBuilder();

        if (ventasRadioBoton.isSelected()) {
            reporte.append("Reporte de Ventas - ").append(fechaSeleccionada).append("\n\n");
            for (Factura f : historial.getFacturas()) {
                reporte.append(f.generarFacturaTexto()).append("\n\n");
            }
        } else if (productosRadioBoton.isSelected()) {
            reporte.append("Reporte de Productos - ").append(fechaSeleccionada).append("\n\n");
            for (Producto p : inventario.getListaProductos()) {
                reporte.append(p.getCodigoProducto()).append(" - ")
                        .append(p.getNombreProducto()).append(" (")
                        .append(p.getCategoriaProducto()).append(")\n")
                        .append("Precio: ₡").append(p.getPrecioProducto()).append(" | Stock: ")
                        .append(p.getCantidadStock()).append("\n\n");
            }
        } else if (clientesRadioBoton.isSelected()) {
            reporte.append("Reporte de Clientes - ").append(fechaSeleccionada).append("\n\n");
            for (Cliente c : gestorClientes.getClientes()) {
                reporte.append(c.getNombre()).append(" ").append(c.getApellido())
                        .append(" | Cédula: ").append(c.getCedula())
                        .append(" | Correo: ").append(c.getCorreo())
                        .append("\n");
            }
        } else {
            javax.swing.JOptionPane.showMessageDialog(this,
                    "Seleccione un tipo de reporte.",
                    "Aviso",
                    javax.swing.JOptionPane.WARNING_MESSAGE);
            return;
        }
        detallesDelReporteTextArea.setText(reporte.toString());
    }//GEN-LAST:event_generarReporteBotonActionPerformed

    private void botonMenuPrincipalActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_botonMenuPrincipalActionPerformed
        this.dispose();
        menuPadre.setVisible(true);
    }//GEN-LAST:event_botonMenuPrincipalActionPerformed

    private void productosRadioBotonActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_productosRadioBotonActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_productosRadioBotonActionPerformed

    private void fechasReportesComboBoxActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_fechasReportesComboBoxActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_fechasReportesComboBoxActionPerformed

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ReflectiveOperationException | javax.swing.UnsupportedLookAndFeelException ex) {
            logger.log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton botonMenuPrincipal;
    private javax.swing.JRadioButton clientesRadioBoton;
    private javax.swing.JTextArea detallesDelReporteTextArea;
    private javax.swing.JComboBox<String> fechasReportesComboBox;
    private javax.swing.JButton generarReporteBoton;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JPanel jPanel2;
    private javax.swing.JPanel jPanel3;
    private javax.swing.JPanel jPanel4;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.ButtonGroup opcionesReportesGrupoBoton;
    private javax.swing.JRadioButton productosRadioBoton;
    private javax.swing.JRadioButton ventasRadioBoton;
    // End of variables declaration//GEN-END:variables
}
