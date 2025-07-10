# Talent Airtable Template Guide

## 📋 **Consolidated Template Overview**

The `talent-airtable-template.csv` eliminates repetitive information from individual talent profiles and creates a streamlined database structure.

## 🔄 **What Was Consolidated**

### **Removed Repetition:**
- ❌ Multiple "Status" fields (now single `Availability Status`)
- ❌ Redundant "Years of Experience" mentions
- ❌ Duplicate location information
- ❌ Repetitive "Pearl Talent" references

### **Streamlined Fields:**
- ✅ Single `Pearl Talent Status` (Current Candidate, Alumni, Placed)
- ✅ Clear `Placement Status` vs `Availability Status`
- ✅ Consolidated location into `Country`, `City`, `Region`
- ✅ Combined skills into single field

## 📊 **Key Field Explanations**

### **Status Fields**
- **Placement Status**: `Available`, `Placed`, `In Process`
- **Availability Status**: `Available`, `Employed`, `On Assignment`
- **Pearl Talent Status**: `Current Candidate`, `Alumni`, `Testimonial`

### **Location Fields**
- **Region**: `Asia Pacific`, `Latin America`, `Africa`, `North America`
- **Country**: Full country name
- **City**: Primary city location

### **Experience Fields**
- **Years of Experience**: Total years in primary role
- **Previous Company**: Most recent/relevant employer
- **Current Company**: If placed through Pearl Talent

## 🎯 **Client Instructions**

### **For Current Candidates:**
```csv
Name,Email,Phone,Country,City,Region,Primary Role,Years of Experience,Previous Company,Current Company,Current Position,Placement Status,Availability Status,...
John Doe,john@email.com,+1-555-0123,USA,Austin,North America,Software Engineer,5,Google,,Available,Available,...
```

### **For Placed Talent:**
```csv
Name,Email,Phone,Country,City,Region,Primary Role,Years of Experience,Previous Company,Current Company,Current Position,Placement Status,Availability Status,...
Jane Smith,jane@email.com,+63-917-123456,Philippines,Manila,Asia Pacific,Executive Assistant,3,BPO Corp,Client Company,Executive Assistant,Placed,Employed,...
```

### **For Alumni/Testimonials:**
```csv
Name,Email,Phone,Country,City,Region,Primary Role,Years of Experience,Previous Company,Current Company,Current Position,Placement Status,Availability Status,Client Testimonial,...
Mike Johnson,,,Philippines,,Asia Pacific,Developer,4,,Startup Inc,Lead Developer,Placed,Employed,"Pearl Talent helped me find my dream job",...
```

## 🚀 **Airtable Setup Instructions**

### **1. Import CSV**
- Upload `talent-airtable-template.csv` to new Airtable base
- Airtable will auto-detect field types

### **2. Recommended Field Types**
- **Name**: Single line text
- **Email**: Email
- **Phone**: Phone number  
- **Placement Status**: Single select (`Available`, `Placed`, `In Process`)
- **Availability Status**: Single select (`Available`, `Employed`, `On Assignment`)
- **Pearl Talent Status**: Single select (`Current Candidate`, `Alumni`, `Testimonial`)
- **Performance Rating**: Number (1-5 scale)
- **Key Skills**: Long text
- **Client Testimonial**: Long text

### **3. Create Views**
- **Available Talent**: Filter by `Availability Status = Available`
- **Placed Talent**: Filter by `Placement Status = Placed`
- **By Region**: Group by `Region`
- **By Role**: Group by `Primary Role`

## 📈 **Benefits of Consolidation**

### **For Pearl Talent:**
- ✅ Single source of truth for all talent data
- ✅ Easy filtering and searching
- ✅ Clear status tracking
- ✅ Reduced data entry errors

### **For Clients:**
- ✅ Simple template to fill out
- ✅ Clear field definitions
- ✅ No redundant information
- ✅ Easy to maintain and update

## 🔄 **Data Flow**

```
Client fills CSV → Uploads to Airtable → Pearl Talent reviews → Talent profiles updated → Knowledge Base sync
```

## 📝 **Next Steps**

1. **Send template to client** with this guide
2. **Schedule review call** to explain fields
3. **Set up Airtable base** when data is received
4. **Create automated sync** to update Knowledge Base profiles

---

*This consolidated approach eliminates the repetitive information found in individual talent files while maintaining all essential data for effective talent management.* 