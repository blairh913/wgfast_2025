# Interoperating Echopype-generated data

Should probably have this in echopype docs!

## Matlab

Matlab provides quite a bit of functionalities to work with netCDF files (see [here](https://www.mathworks.com/help/matlab/network-common-data-form.html)). This [Import NetCDF Files and OPeNDAP Data](https://www.mathworks.com/help/matlab/import_export/importing-network-common-data-form-netcdf-files-and-opendap-data.html) page in particular shows a nice example walking through various functions.

```{tip}
Here we only cover netCDF files, but Matlab also has a set of functions to work with Zarr files in [this repository](https://github.com/mathworks/MATLAB-support-for-Zarr-files).
```

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

&nbsp;

## R

There are a several  different packages that allow you to work with netCDF data in R including, `stars`, `netCDF`, `netCDF4`, `terr`, `metR1`, `RNetCDF`, and `tidcync`

We will use `tidync` to read in and plot netCDF data exported from [Echopype](https://github.com/OSOceanAcoustics/echopype).

`tidync` was developed and maintained by
[ROpenSci](https://github.com/ropensci/tidync/tree/main)

### Install

If you do not have the package in your library folder, install the stable version from CRAN:

``` r
install.packages("tidync")
```

Or, you can install the developmental version from GitHub. You will need the `remotes` package to do this.

``` r
install.packages("remotes")
remotes::install_github("ropensci/tidync", dependencies = TRUE)
```

### Attach packages

``` r
library(tidync)
library(dplyr)
library(ggplot2)
library(lubridate)
```

### Load the data

The .nc data file is in the tutorials/resources folder of this repository. First set a path to the data folder using the `here` package, then load the file using `tidync`.

``` r
# path to data folder
dta <- here::here("tutorials/resources")
```

We are only going to use one function from the `here` package, so we are not going to attach it to our session like we did by calling the other packages with `library()`. By using the package name and `::` we can call a function from the package (assuming it is in your library folder). We are using `here()` instead of `setwd()` because `here()` enables easy file referencing by using the your top-level directory (folder) to build file paths. Use `paste0()` to concatenate the file path and file name.

paste0(dta, “/test_MVBS.nc”) -\> “path to your repository/tutorials/resources/test_MVBS.nc”

``` r
# load data - retrieve both values in the data array and the metadata with tidync()
mvbs <- tidync(paste0(dta, "/test_MVBS.nc"))
```
### Examine the data structure

``` r
# show data
mvbs
```

    ## 
    ## Data Source (1): test_MVBS.nc ...
    ## 
    ## Grids (4) <dimension family> : <associated variables> 
    ## 
    ## [1]   D2,D1,D0 : Sv    **ACTIVE GRID** ( 419580  values per variable)
    ## [2]   D0       : channel, frequency_nominal
    ## [3]   D1       : ping_time, latitude, longitude
    ## [4]   D2       : depth
    ## 
    ## Dimensions 3 (all active): 
    ##   
    ##   dim   name      length   min   max start count  dmin  dmax unlim coord_dim 
    ##   <chr> <chr>      <dbl> <dbl> <dbl> <int> <int> <dbl> <dbl> <lgl> <lgl>     
    ## 1 D0    channel        3    NA    NA     1     3    NA    NA FALSE TRUE      
    ## 2 D1    ping_time    180     0   895     1   180     0   895 FALSE TRUE      
    ## 3 D2    depth        777     0   388     1   777     0   388 FALSE TRUE

Under dimensions, `unlim == FALSE` means that the extent of the data are fixed. `coord_dim == TRUE` means that the dimension being used is attached o the dataset. In larger datasets, you might not want to bring in all the data.

Use `hyper_dims()` to inspect the dimensions in more detail.

``` r
hyper_dims(mvbs)
```

    ## # A tibble: 3 × 7
    ##   name      length start count    id unlim coord_dim
    ##   <chr>      <dbl> <int> <int> <int> <lgl> <lgl>    
    ## 1 depth        777     1   777     2 FALSE TRUE     
    ## 2 ping_time    180     1   180     1 FALSE TRUE     
    ## 3 channel        3     1     3     0 FALSE TRUE

&nbsp;

Use `hyper_vars()` to explore the variable - Sv.

``` r
hyper_vars(mvbs)
```

    ## # A tibble: 1 × 6
    ##      id name  type      ndims natts dim_coord
    ##   <int> <chr> <chr>     <int> <int> <lgl>    
    ## 1     0 Sv    NC_DOUBLE     3     7 FALSE

### Examine the data values

To access the data values, you have to active the correct grid with `activate()`, then extract the values with `hyper_tibble()`.

Use `glimpse()` to view the data types and the first few values.

``` r
ping_data <- mvbs %>% 
  activate(Sv) %>% 
  hyper_tibble()

glimpse(ping_data)
```

    ## Rows: 409,320
    ## Columns: 4
    ## $ Sv        <dbl> -4.291311, -39.067087, -45.867860, -61.991222, -70.152770, -…
    ## $ depth     <chr> "9.5", "10", "10.5", "11", "11.5", "12", "12.5", "13", "13.5…
    ## $ ping_time <chr> "2017-07-26T02:35:00", "2017-07-26T02:35:00", "2017-07-26T02…
    ## $ channel   <chr> "GPT  18 kHz 009072058c8d 1-1 ES18-11", "GPT  18 kHz 0090720…

&nbsp;

Sv is stored as double, but depth and ping_time are stored as characters. These need to be changed to double and datetime respectively.

``` r
ping_data <- ping_data %>%  
  mutate(depth = as.numeric(depth),
         ping_time = ymd_hms(ping_time))

glimpse(ping_data)
```

    ## Rows: 409,320
    ## Columns: 4
    ## $ Sv        <dbl> -4.291311, -39.067087, -45.867860, -61.991222, -70.152770, -…
    ## $ depth     <dbl> 9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 1…
    ## $ ping_time <dttm> 2017-07-26 02:35:00, 2017-07-26 02:35:00, 2017-07-26 02:35:…
    ## $ channel   <chr> "GPT  18 kHz 009072058c8d 1-1 ES18-11", "GPT  18 kHz 0090720…

&nbsp;

### Plot

We will use the ggplot2 package with `geom_tile()` to plot the echograms. 

``` r
ping_data %>% 
  ggplot(aes(ping_time, depth, color = Sv)) +
  geom_tile() +
  scale_y_reverse() +
  scale_color_viridis_c(limits = c(-100, -20)) +
  facet_wrap(~channel, nrow = 3) +
  theme_minimal() +
  theme(legend.title = element_text(angle = 90, hjust = 0.5),
        legend.title.position = "right") +
  labs(x = "Ping time",
       y = "Range distance (m)",
       color = "Mean volume backscatteing strength
       (MVBS, mean Sv re 1 m-1) [dB]")
```

&nbsp;

```{image} ./images/tool/R_echogram.png
:width: 1000px
:align: center
```

&nbsp; 

```{note} R Users can find an .Rmd file of all the R code is in a separate repository here: https://github.com/erinann/WGFAST-2025-NetCDF-Tutorial
```

example scripts

- echodata object
- Sv xarray Dataset
