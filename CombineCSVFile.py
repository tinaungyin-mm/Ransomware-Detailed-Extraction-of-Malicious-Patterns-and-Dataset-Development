import pandas as pd

# Read the two CSV files
output_df = pd.read_csv('C:/Users/RansomwareLab/Desktop/Final Outputs/goodware_volfeature.csv')
speakclean_df = pd.read_csv('C:/Users/RansomwareLab/Desktop/Final Outputs/goodware_speakfeature.csv')

# Perform the join operation based on md5_hash column
merged_df = output_df.merge(speakclean_df, on='md5_hash', how='inner')

# Drop the md5_hash column
#merged_df.drop('md5_hash', axis=1, inplace=True)

# Export the merged DataFrame as formated.csv
merged_df.to_csv('C:/Users/RansomwareLab/Desktop/Final Outputs/goodware_finalfeatures.csv', index=False)

print('Join operation completed. Merged data exported to formated.csv.')
