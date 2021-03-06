# Generated by Django 2.0.6 on 2019-03-06 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Afiliado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_afiliacion', models.DateField(blank=True, null=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('sexo', models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=12)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('documento', models.CharField(max_length=50, unique=True)),
                ('mensualidad', models.FloatField(blank=True, null=True)),
                ('distrito', models.CharField(blank=True, max_length=50)),
                ('direccion', models.CharField(blank=True, max_length=200)),
                ('prefijo', models.CharField(blank=True, default=57, max_length=200)),
                ('telefono', models.CharField(blank=True, max_length=50, verbose_name='telefono (Movil)')),
                ('fijo', models.CharField(blank=True, max_length=50, verbose_name='telefono (Fijo)')),
                ('email', models.EmailField(blank=True, max_length=50, verbose_name='Correo electrónico')),
                ('estatus', models.CharField(blank=True, choices=[('1', 'Activo'), ('0', 'Retirado')], default=1, max_length=12)),
                ('epsactual', models.CharField(blank=True, max_length=50, verbose_name='Eps donde se Encuentra Actualmente')),
                ('epstraslado', models.CharField(blank=True, max_length=50, verbose_name='Eps a donde quiere ser Trasladado')),
                ('pinseguridadsocial', models.CharField(blank=True, max_length=15, verbose_name='PIN con que ingresa Seguridad Social')),
            ],
            options={
                'verbose_name_plural': 'Afiliados',
            },
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Ciudades',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('documento', models.CharField(max_length=50)),
                ('telefono', models.CharField(blank=True, max_length=50, verbose_name='telefono (Movil)')),
            ],
        ),
        migrations.CreateModel(
            name='EmpresaAfiliada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('nit', models.CharField(blank=True, max_length=50, unique=True)),
                ('telefono', models.CharField(blank=True, max_length=50, verbose_name='Telefono de la Empresa')),
            ],
            options={
                'verbose_name_plural': 'Empresas Afiliadas',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='EmpresaSeguridadSocial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('telefonos1', models.CharField(blank=True, max_length=50, verbose_name='telefono (Fijo)')),
                ('telefonos2', models.CharField(blank=True, max_length=50, verbose_name='telefono (Opcional)')),
                ('direccion', models.CharField(blank=True, max_length=200)),
                ('horario', models.CharField(blank=True, max_length=70, verbose_name='Horario de Atencion')),
                ('nombreasesor', models.CharField(blank=True, max_length=50, verbose_name='Nombre del Asesor')),
                ('telefonoAsesor', models.CharField(blank=True, max_length=50, verbose_name='Telefono del Asesor')),
            ],
            options={
                'verbose_name_plural': 'Empresas Seguridad Social',
            },
        ),
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(blank=True, max_length=50)),
                ('documento', models.CharField(blank=True, max_length=50)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('afiliado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='afiliados.Afiliado')),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pago', models.DateField(blank=True, null=True)),
                ('monto', models.FloatField(blank=True, null=True)),
                ('recibo', models.IntegerField(blank=True, null=True)),
                ('observacion', models.CharField(blank=True, max_length=50, verbose_name='Concepto de pago')),
                ('foto', models.ImageField(default='Foto recibo de Pago', upload_to='Consignaciones/')),
                ('afiliado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='afiliados.Afiliado', verbose_name='Quién realizó el Pago?')),
            ],
        ),
        migrations.CreateModel(
            name='PagoEmpresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pago', models.DateField(blank=True, null=True)),
                ('monto', models.FloatField(blank=True, null=True)),
                ('recibo', models.IntegerField(blank=True, null=True)),
                ('observacion', models.CharField(blank=True, max_length=50, verbose_name='Concepto de pago')),
                ('foto', models.ImageField(default='Foto recibo de Pago', upload_to='Consignaciones/')),
                ('empresaafiliada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='afiliados.EmpresaAfiliada', verbose_name='Quién realizó el Pago?')),
            ],
        ),
        migrations.CreateModel(
            name='Rango',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoServicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vinculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='familia',
            name='tipoDoc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='afiliados.TipoDocumento', verbose_name='Tipo de Documento'),
        ),
        migrations.AddField(
            model_name='familia',
            name='vinculo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='afiliados.Vinculo'),
        ),
        migrations.AddField(
            model_name='empresaseguridadsocial',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='afiliados.TipoServicio'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='empresaafiliada',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='afiliados.EmpresaAfiliada', verbose_name='Quién realizó el Pago?'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='tipoDoc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='afiliados.TipoDocumento', verbose_name='Tipo de Documento'),
        ),
        migrations.AddField(
            model_name='afiliado',
            name='ciudad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='afiliados.Ciudad'),
        ),
        migrations.AddField(
            model_name='afiliado',
            name='departamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='afiliados.Departamento'),
        ),
        migrations.AddField(
            model_name='afiliado',
            name='rango',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='afiliados.Rango'),
        ),
        migrations.AddField(
            model_name='afiliado',
            name='servicios',
            field=models.ManyToManyField(blank=True, to='afiliados.TipoServicio', verbose_name='servicios'),
        ),
        migrations.AddField(
            model_name='afiliado',
            name='tipoDoc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='afiliados.TipoDocumento', verbose_name='Tipo de Documento'),
        ),
    ]
