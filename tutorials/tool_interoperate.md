# Interoperating Echopype-generated data

Should probably have this in echopype docs!


## Matlab

Matlab provides quite a bit of functionalities to work with netCDF files (see [here](https://www.mathworks.com/help/matlab/network-common-data-form.html)). This [Import NetCDF Files and OPeNDAP Data](https://www.mathworks.com/help/matlab/import_export/importing-network-common-data-form-netcdf-files-and-opendap-data.html) page in particular shows a nice example walking through various functions.

Below is a simple example showing how to use `ncinfo`, `ncdisp`, `ncread`, and `ncreadatt` to read and plot an Echopype-generated MVBS dataset. The file we use here is located in the path: `/tutorials/resources/test_MVBS.nc` if you want to give the below commands a try.

To figure out what the dimensions and variable are in this netCDF file, we use `ncinfo`:
```matlab
>> ncinfo("test_MVBS.nc")

ans = 

  struct with fields:

      Filename: 'test_MVBS.nc'
          Name: '/'
    Dimensions: [1×3 struct]
     Variables: [1×4 struct]
    Attributes: []
        Groups: []
        Format: 'netcdf4'
     Datatypes: []
```
Since this is a `struct`, we can then inspect the dimensions and variables. For example, to see what variable names are:
```matlab
>> nc_content = ncinfo("test_MVBS.nc");
>> nc_content

nc_content = 

  struct with fields:

      Filename: 'test_MVBS.nc'
          Name: '/'
    Dimensions: [1×3 struct]
     Variables: [1×7 struct]
    Attributes: [1×6 struct]
        Groups: []
        Format: 'netcdf4'
     Datatypes: []

>> nc_content.Variables.Name

ans =

    'Sv'


ans =

    'ping_time'


ans =

    'channel'


ans =

    'depth'


ans =

    'latitude'


ans =

    'longitude'


ans =

    'frequency_nominal'
```

We then can use `ncread` to read `Sv`, `ping_time`, and `depth`, in order to plot an echogram.
```matlab
Sv = ncread("test_MVBS.nc", "Sv");
ping_time = ncread("test_MVBS.nc", "ping_time");
depth = ncread("test_MVBS.nc", "depth");
```

The values in `Sv` and `ping_time` seems normal, but when we inspect `ping_time`, we found that they are in `int64` type!
```matlab
>> ping_time(1:5)

ans =

  5×1 int64 column vector

    0
    5
   10
   15
   20
```

Digging further, we found that the output of `ncdisp("/Users/wujung/Downloads/hake_2017_x52_0.nc")` includes:
```matlab
    ping_time        
           Size:       180x1
           Dimensions: ping_time
           Datatype:   int64
           Attributes:
                       long_name     = 'Ping time'
                       standard_name = 'time'
                       axis          = 'T'
                       units         = 'seconds since 2017-07-26 02:35:00'
                       calendar      = 'proleptic_gregorian'
```
which tells us that the integer `ping_time` we saw above are counted from a particular start time.

To plot the echogram with the appropriate `ping_time`, let's construct an array of ping times in the matlab `datetime` type using the information in `units`:
```matlab
ping_time_datetime = datetime(2017,7,26,2,35,0+ping_time);
```

Now we are ready to plot!

We know we can use `imagesc` to quickly plot the echogram, since the `depth` and `ping_time` are regularly spaced in the MVBS dataset. However, it turns out to directly use an array of `datetime` type (such as the `ping_time_datetime` we just constructed) to plot the x-axis, one needs to have **at least Matlab version `R2023b`**.

If you have Matlab version `R2023b` or newer, you can simply plot the echogram using:
```matlab
imagesc(depth, ping_time_datetime, Sv);
```

However, if you only have an older version of Matlab, you can use the following workaround (from [here](https://www.mathworks.com/matlabcentral/answers/1634620-imagesc-or-equivalent-with-datetime-as-x-axis#answer_881580)):
```matlab
imagesc(Sv(:,:,2));
xticks = 20:50:180;  % plot ticks with 20 ping_time spacing
xlabels = cellstr(ping_time_datetime(xticks));
set(gca, 'XTick',xticks, 'XTickLabel', xlabels)
set(gca, 'fontsize', 12)
ylabel('Depth (m)')
clim([-80, -30])
colorbar
```

Which will gives us the following figure:


```{image} ./images/tool/matlab_echogram.png
:width: 600px
:align: center
```




## R

example scripts
- echodata object
- Sv xarray Dataset
