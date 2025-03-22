# Solis Cloud Control API Integration

> Note: This fork is for minimal testing, only base read and write services are enabled

This is very initial version of the Solis Cloud Control API integration for Home Assistant.
It allows you to read and control various settings of your Solis inverter.
Doesn't support sensors, switches, or other entities yet - only basic read and control actions crafted for automations.

See [issue tracker](https://github.com/mkuthan/solis-cloud-control/issues) for further plans.

## Local run

Configure Solis Cloud Control API credentials in `secrets.yaml`:

```yaml
solis_api_key: "YOUR_API_KEY_HERE"
solis_token: "YOUR_TOKEN_HERE"
solis_inverter_sn: "YOUR_INVERTER_SN_HERE"
```

Install dependencies (once):

```bash
uv sync
```

Run the integration locally:

```bash
./scripts/run
```

## Read inverter settings

Storage Mode

```yaml
action: solis_cloud_control.read
data:
  cid: 636
```

## Low-level inverter control

### Control storage mode

Self-Use Mode - Battery Reserve On, Grid Charging Off:

```yaml
action: solis_cloud_control.control
data:
  cid: 636
  value: "17"
```

Feed-In Priority Mode - Battery Reserve On, Grid Charging Off:

```yaml
action: solis_cloud_control.control
data:
  cid: 636
  value: "80"
```

### Control charge time slot

Set Charge Time Slot 1:

```yaml
action: solis_cloud_control.control
data:
  cid: 5946
  value: "11:00-13:00"
```

Set Charge Time Slot 1 Current:

```yaml
action: solis_cloud_control.control
data:
  cid: 5948
  value: "90"
```

Set Charge Time Slot 1 Battery SOC:

```yaml
action: solis_cloud_control.control
data:
  cid: 5928
  value: "80"
```

### Control discharge time slot

Set Discharge Time Slot 1:

```yaml
action: solis_cloud_control.control
data:
  cid: 5964
  value: "11:00-13:00"
```

Set Discharge Time Slot 1 Current:

```yaml
action: solis_cloud_control.control
data:
  cid: 5967
  value: "90"
```

Set Discharge Time Slot 1 Battery SOC:

```yaml
action: solis_cloud_control.control
data:
  cid: 5965
  value: "80"
```
